import jieba

from pyscript.Question import question

jieba.initialize()  # 初始化


class wordCoverage:
    # 通过分词后词组的覆盖率对比
    coverage = None
    str1_list = ""
    str2 = ""
    str_qes = ""

    def __init__(self, str1_list, str2, str_qus):
        self.str1_list = str1_list
        self.str2 = str2
        self.str_qes = str_qus
        self.coverage = self.cover()

    def cover(self):
        num = 0
        for i in self.str1_list:
            if i in self.str2:
                num += 1
        if self.str_qes in self.str2:
            k = 1
            return k
        return num / len(self.str1_list)


class searchAns:
    ques_str = ""  # 要搜索的题目文本
    best_match = question()

    def __init__(self, ques):
        self.ques_str = self.formatstr(ques)

    def formatstr(self, ques):
        ques = str(ques)
        return ques.replace(" ", "").replace("\n", "").replace("\t", "")

    # import Levenshtein
    # def basedistance(self, ques_bank):
    #     # 莱温斯坦距离也是一个很好的对比方法，但对于较短的句子可能不太合适
    #     min_dis = 99999
    #     for i in ques_bank:
    #         distance = Levenshtein.distance(self.ques_str, i.get_ques_text())
    #         if distance == 0:
    #             self.best_match = i
    #             break
    #         elif distance < min_dis:
    #             min_dis = distance
    #             self.best_match = i
    #         else:
    #             pass
    #     return self.best_match

    def basecover(self, ques_bank):
        # 在这种算法下，如果str1是一个适当的长度字符串那么返回结果很好
        max_cover = 0
        for i in ques_bank:
            split = list(jieba.cut(self.ques_str, cut_all=False))
            cover = wordCoverage(str1_list=split, str2=i.get_ques_text(), str_qus=self.ques_str).coverage
            if cover == 1:
                self.best_match = i
                break
            elif cover >= max_cover:
                self.best_match = i
                max_cover = cover
            else:
                pass
        return self.best_match
