
from query import Query


class QuestionTemplate:
    def __init__(self):
        self.q_template_dict = {
            0: self.get_info,
            1: self.get_build_time,
            2: self.get_leader,
            3: self.get_college,
            4: self.get_web,
            5: self.get_departments,
            6: self.get_pp_professional_title,
            7: self.get_pp_department,
            8: self.get_pp_research,
        }

        # 连接数据库
        self.graph = Query()

    def get_question_answer(self, question, template):
        # 如果问题模板的格式不正确则结束
        assert len(str(template).strip().split("\t")) == 2
        template_id,template_str=int(str(template).strip().split("\t")[0]),str(template).strip().split("\t")[1]
        self.template_id = template_id
        self.template_str2list = str(template_str).split()

        # 预处理问题
        question_word, question_flag = [], []
        for one in question:
            word, flag = one.split("/")
            question_word.append(str(word).strip())
            question_flag.append(str(flag).strip())
        assert len(question_flag) == len(question_word)
        self.question_word = question_word
        self.question_flag = question_flag
        self.raw_question = question
        # 根据问题模板来做对应的处理，获取答案
        answer = self.q_template_dict[template_id]()
        return answer

    # 获取南开大学相关名词
    def get_name(self, type_str):
        # 获取nk或pp在原问题中的下标
        tag_index = self.question_flag.index(type_str)
        # 获取南开相关名词
        name = self.question_word[tag_index]
        return name

    # 0:nk 简介
    def get_info(self):
        nk_name = self.get_name('nk')
        cql = f"match(n:NK) where n.name='{nk_name}' return n.info"
        print(cql)
        answer = self.graph.run(cql)[0]
        final_answer = answer
        return final_answer

    # 1:nk 成立时间
    def get_build_time(self):
        nk_name = self.get_name('nk')
        cql = f"match (n:NK) where n.name='{nk_name}' return n.buildtime"
        print(cql)
        answer = self.graph.run(cql)[0]
        final_answer = nk_name + "的成立时间为" + str(answer)
        return final_answer

    # 2:nk 领导
    def get_leader(self):
        nk_name = self.get_name('nk')
        cql = f"match(n:NK) where n.name='{nk_name}' return n.leader"
        print(cql)
        answer = self.graph.run(cql)[0]
        final_answer = nk_name + "的现任领导有" + str(answer)
        return final_answer

    # 3:nk 学院
    def get_college(self):
        nk_name = self.get_name('nk')
        cql = f"match(n:NK) where n.name='{nk_name}' return n.college"
        print(cql)
        answer = self.graph.run(cql)[0]
        final_answer = nk_name + "的学院有" + str(answer)
        return final_answer

    # 4:nk 网址
    def get_web(self):
        nk_name = self.get_name('nk')
        cql = f"match(n:NK) where n.name='{nk_name}' return n.web"
        print(cql)
        answer = self.graph.run(cql)[0]
        final_answer = nk_name + "的网址是" + str(answer)
        return final_answer

    # 5:nk 职能部门
    def get_departments(self):
        nk_name = self.get_name('nk')
        cql = f"match(n:NK) where n.name='{nk_name}' return n.departments"
        print(cql)
        answer = self.graph.run(cql)[0]
        final_answer = nk_name + "的职能部门有" + str(answer)
        return final_answer

    # 6:pp 职称
    def get_pp_professional_title(self):
        pp_name = self.get_name("pp")
        cql = f"match(p:Person)-[r:pt]->(t) where p.name='{pp_name}' return t.name"
        print(cql)
        answer = self.graph.run(cql)[0]
        final_answer = pp_name + "老师的职称是" + str(answer)
        return final_answer

    # 7:pp 所属部门
    def get_pp_department(self):
        pp_name = self.get_name("pp")
        cql = f"match(p:Person)-[r:in]->(d) where p.name='{pp_name}' return d.name"
        print(cql)
        answer = self.graph.run(cql)[0]
        final_answer = pp_name + "老师的所属部门是" + str(answer)
        return final_answer

    # 8:pp 研究方向
    def get_pp_research(self):
        pp_name = self.get_name("pp")
        cql = f"match(p:Person) where p.name='{pp_name}' return p.research"
        print(cql)
        answer = self.graph.run(cql)[0]
        final_answer = pp_name + "老师的研究方向是" + str(answer)
        return final_answer


