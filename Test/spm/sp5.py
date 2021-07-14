import json

kl = json.load(open('url4.json', 'r', encoding='utf8'))

list_couse_5 = []
for i in kl:
    for k in i:
        list_couse_5.append('https://tes.tmooc.cn/qsexam/QSRandomPaperExam?courseId='+k["courseId"])

f = open("url5.json", 'w', encoding='utf8')

f.write(json.dumps(list_couse_5, ensure_ascii=False) + '\n')
