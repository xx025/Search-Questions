
# simply sqlite database remove duplicate

#import sqlite3

# import setting
#
# DATABASE = setting.setting.sqlite_db
# conn = sqlite3.connect(DATABASE)
# c = conn.cursor()
#
# qbk = c.execute("select DISTINCT * from qus_bank")
#
# print(type(qbk))
#
# dix = [i for i in qbk]
#
#
# K=0
# for data in dix:
#     K+=1
#     print(str(K)+""+str(dix.__len__()))
#     c.execute("insert into  question_bank values (?,?,?,?)", data)
#     conn.commit()
