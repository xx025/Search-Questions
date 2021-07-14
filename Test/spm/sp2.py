import json

kl = json.load(open('url2.json', 'r', encoding='utf8'))

list_couse_3 = []
for i in kl:
    dic1 = {"courseId": i["courseId"],
            "courseName": i["courseName"]}
    list_this_2 = []
    for k in i["course_list"]:
        list_this_2.append({"courseId": k["courseId"],
                            "courseName": k["courseName"]})
    dic1["course_list"] = list_this_2
    list_couse_3.append(dic1)


f = open("url3.json", 'w', encoding='utf8')

f.write(json.dumps(list_couse_3, ensure_ascii=False) + '\n')