
# '''
# 针对word文档的题库抽取题目，将word转换为txt文本
# '''
# import json
#
# from Question import question
#
# ques_list = []
# ques_text = ""
# options = []
# solution = ""
# explainAns = ""
#
#
# def init_param():
#     global ques_list
#     global ques_text
#     global options
#     global solution
#     global explainAns
#     quu = question(questionText=ques_text, options=options, solution=solution, explainAns=explainAns)
#     ques_list.append(quu)
#     ques_text = ""
#     options = []
#     solution = ""
#     explainAns = ""
#
#
# def transport(lin):
#     global ques_list
#     global ques_text
#     global options
#     global solution
#     global explainAns
#     if lin.find("答案解析") > -1:
#         explainAns = lin
#         init_param()
#     elif lin.find("正确答案") > -1:
#         solution = lin
#     elif lin.find("."):
#         if lin[0:lin.find(".")].isalpha() and lin[0:lin.find(".")].__len__() == 1:
#             options.append({"optionContent": lin, "isCorrect": "-1"})
#         else:
#             ques_text += lin
#     elif lin.find("、") > -1:
#         if lin[0:lin.find("、")].isdigit():
#             ques_text += lin
#     else:
#         ques_text += lin
#
#
# f = open(file='quesBank/新建文本文档.txt', encoding="utf8")
#
# while True:
#     try:
#         line = f.__next__()
#         transport(line)
#     except:
#         break
#
# kk = [i.get_self() for i in ques_list]
# with open('../quesbank/questionbank1.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps({"questionBank": kk}, ensure_ascii=False) + '\n')



# '''
#
# json file stor in databse
# '''
#
#
# import json
# import sqlite3
#
# import setting
#
# kk = None
# with open("db/questionbank1.json", "r", encoding='utf8') as f:
#     kk = json.load(f)
#
# DATABASE = setting.setting.sqlite_db
#
# conn = sqlite3.connect(DATABASE)
# c = conn.cursor()
#
# sum = len(kk['questionBank'])
# now = 0
# for i in kk['questionBank']:
#     # mynewdic = eval(mystr)
#     data = (str(i["questionText"]), str(i["options"]), i["explainAns"], i["solution"])
#     c.execute("insert into  question_bank values (?,?,?,?)", data)
#     conn.commit()
#     now += 1
#     print( now/ sum)
# conn.close()

