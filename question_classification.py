
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import re
import jieba
import pickle


# 获取所有的文件
def get_file_list(root_path):
    file_path_list = []
    file_name = []
    walk = os.walk(root_path)
    for root, dirs, files in walk:
        for name in files:
            filepath = os.path.join(root, name)
            file_name.append(name)
            file_path_list.append(filepath)
    return file_path_list


class QuestionClassify:
    def __init__(self):
        # 读取训练数据
        self.train_x, self.train_y = self.read_train_data()
        # 训练模型
        self.model = self.train_model_NB()

    # 获取训练数据
    def read_train_data(self):
        train_x = []
        train_y = []
        file_list = get_file_list("./data/question/")
        # 遍历所有文件
        for one_file in file_list:
            # 获取文件名中的数字
            num = re.sub(r'\D', "", one_file)
            # 如果该文件名有数字，则读取该文件
            if str(num).strip() != "":
                # print(num)
                # 设置当前文件下的数据标签
                label_num = int(num)
                # 读取文件内容
                with(open(one_file, "r", encoding = "utf-8")) as fr:
                    data_list = fr.readlines()
                    for one_line in data_list:
                        word_list = list(jieba.cut(str(one_line).strip()))
                        # 将这一行加入结果集
                        train_x.append(" ".join(word_list))
                        train_y.append(label_num)
        return train_x, train_y

    # 训练并测试模型-NB
    def train_model_NB(self):
        X_train, y_train = self.train_x, self.train_y
        self.tv = TfidfVectorizer()

        train_data = self.tv.fit_transform(X_train).toarray()
        clf = MultinomialNB(alpha = 0.01)
        clf.fit(train_data, y_train)

        # 保存成Python支持的文件格式Pickle
        # 保存再读取无法获得self.tv，不行
        # with open('model.pickle', 'wb') as fw:
        #     pickle.dump(clf, fw)
        return clf

    # 预测
    def predict(self, question):
        question = [" ".join(list(jieba.cut(question)))]
        test_data = self.tv.transform(question).toarray()
        y_predict = self.model.predict(test_data)[0]
        # print("question type:", y_predict)
        return y_predict


if __name__ == '__main__':
    qc = QuestionClassify()
    qc.predict("南开大学的成立时间")
