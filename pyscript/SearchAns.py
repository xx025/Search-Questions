import logging

import Levenshtein
import jieba

from pyscript.Question import question

jieba.setLogLevel(logging.INFO)
jieba.initialize()  # 初始化


class base_cover:
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
        if self.str_qes in self.str2:
            k = 1
            return k
        else:
            for i in self.str1_list:
                if i in self.str2:
                    num += 1
            return num / len(self.str1_list)


class base_leven():
    distance = 9999
    str2 = ""
    str1 = ""

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.distance = Levenshtein.distance(str1, str2)


class searchAns:
    ques_str = ""  # 要搜索的题目文本
    best_match = question()

    def __init__(self, ques):
        self.ques_str = self.formatstr(ques)

    def formatstr(self, ques):
        ques = str(ques)
        return ques.replace(" ", "").replace("\n", "").replace("\t", "")

    def get_ans(self, ques_bank):
        max_cover = 0
        best_match_list = []  # 记录分词覆盖率相同的
        for i in ques_bank:
            split = list(jieba.cut(self.ques_str, cut_all=False))
            cover = base_cover(str1_list=split, str2=i.get_ques_text(), str_qus=self.ques_str).coverage
            if cover == 1:
                self.best_match = i
                break
            elif cover == max_cover:
                best_match_list.append(i)
            elif cover >= max_cover:
                self.best_match = i
                max_cover = cover
                best_match_list = []  # 清空基于分词覆盖相同覆盖率的列表
        else:
            min_dis = 99999
            for k in best_match_list:
                distance = base_leven(str1=self.ques_str, str2=i.get_ques_text()).distance
                if distance == 0:
                    self.best_match = k
                elif distance <= min_dis:
                    min_dis = distance
                    self.best_match
                else:
                    pass
        return self.best_match
