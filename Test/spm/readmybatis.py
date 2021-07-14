# test sqlite DB read and tansfer json
#
# import sqlite3
#
# import setting
#
# question_bank = []
# DATABASE = setting.setting.sqlite_db
# conn = sqlite3.connect(DATABASE)
# c = conn.cursor()
#
# def valee(strk):
#
#     try:
#         return eval(strk)
#     except:
#         strk
#
# qbk = c.execute("select * from question_bank")
# for i in qbk:
#     question_bank.append([valee(k) for k in i])
#     print([k for k in i])
# conn.close()
