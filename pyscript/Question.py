class question:
    questionText = ""  # 题目问题
    options = []  # 选项列表
    explainAns = ""  # 答案解析
    solution = ""  # 题目解答
    ##########################
    ques_str = ""  # 题目文本拼接

    def __init__(self, questionText="", options=list(), solution="", explainAns=""):
        self.questionText = questionText
        self.options = options
        self.solution = solution
        self.explainAns = explainAns

    def get_ques_text(self):
        ques = ""
        for i in self.options:
            ques += i["optionContent"]
        return (self.questionText + ques).replace("\n", "").replace("\t", "").replace(" ", "")

    # def get_right_ans_str(self):
    #     right_ans_str = ""
    #     for i in self.options:
    #         if i["isCorrect"] == "1":
    #             right_ans_str += i["optionContent"]
    #     return right_ans_str
    #
    # def get_solution(self):
    #     return self.solution

    def get_self(self):
        return {
            "questionText": self.questionText,
            "explainAns": self.explainAns,
            "solution": self.solution,
            "options": self.options
        }

    def get_self_str(self):
        ques = ""
        for i in self.options:
            ques += i["optionContent"]
        return self.questionText + ques +"\n answer:" +self.solution +'\n analysis:'+ self.explainAns
