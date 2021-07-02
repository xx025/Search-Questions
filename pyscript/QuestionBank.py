import sqlite3

import setting
from pyscript.Question import question


class ques_bank:
    ques_bank = []  # 题库

    def __init__(self):
        for i in self.condb():
            ques1 = question(questionText=i[0],
                             options=i[1],
                             explainAns=i[2],
                             solution=i[3])
            self.ques_bank.append(ques1)

    def condb(self):
        def val_cover(strk):
            try:
                return eval(strk)
            except:
                return strk

        question_bank = []
        DATABASE = setting.setting.sqlite_db
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        qbk = c.execute("select DISTINCT * from question_bank")
        for i in qbk:
            question_bank.append([val_cover(k) for k in i])
        conn.close()
        return question_bank

    def get_ques_bank(self):
        return self.ques_bank
