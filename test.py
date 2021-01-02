from question import Question

# 创建问题处理对象，这样模型就可以常驻内存
que = Question()

if __name__ == '__main__':

    q = "袁晓洁老师在什么部门"
    print("问题：", q)
    result = que.question_process(q)
    print("回答：", result)
