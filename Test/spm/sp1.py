# 遍历题库所有课程以及课程下的章节
import json

import requests

kl = json.load(open(r'D:\GitHub\Search-Questions\Test\spm\urlisl.json', 'r', encoding='utf8'))


def get_course_list(course_id):
    # sleep(0.5)
    response = requests.post('https://tes.tmooc.cn/qsexam/CourseLabelListByPid', {'courseId': course_id})
    tp = json.loads(response.text)
    return tp


list_couse = []
for i in kl:
    this_course_info = {'courseId': i['courseId'], 'courseName': i['courseName'],
                        'course_list': get_course_list(course_id=i['courseId'])}
    list_couse.append(this_course_info)

f = open("url2.json", 'w', encoding='utf8')

f.write(json.dumps(list_couse, ensure_ascii=False) + '\n')



