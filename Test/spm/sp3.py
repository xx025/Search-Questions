import json
from time import sleep

import requests

kl = json.load(open('url3.json', 'r', encoding='utf8'))


def get_cip_list(course_id):
    response = requests.post('https://tes.tmooc.cn/qsexam/CourseLabelListByPid', {'courseId': course_id})
    tp = json.loads(response.text)
    return tp


list_course_4 = []
for i in kl:
    for k in i["course_list"]:
        print(k)
        sleep(3)
        list_course_4.append(get_cip_list(k['courseId']))

f = open("url4.json", 'w', encoding='utf8')

f.write(json.dumps(list_course_4, ensure_ascii=False) + '\n')
