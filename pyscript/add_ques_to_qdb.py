import json
import sqlite3

from flask import request

import setting


def add_ques():
    DATABASE = setting.setting.sqlite_db
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    student_json = json.loads(request.data)  # return x:dict()
    for i in student_json['questext']:
        op_list = []
        for k in i['optionList']:
            kl = dict()
            kl['optionContent'] = str(k['option']) + "." + str(k['optionValue'])
            kl['optionContent'] = kl['optionContent'].replace('<xmp>', "").replace('<xmp>', "").replace('</xmp>',
                                                                                                        "").replace(
                '<xmp>', "")
            kl['isCorrect'] = "-1"

            kl['option'] = k['option'].replace('<xmp>', "").replace('</xmp>', "").replace('<xmp>', "")  # 后续做兼容
            kl['optionValue'] = k['optionValue'].replace('<xmp>', "").replace('</xmp>', "").replace('<xmp>', "")  #
            op_list.append(kl)
        print(i)
        try:
            date2 = i['analysis'].replace('<xmp>', "").replace('</xmp>', "").replace('<xmp>', "")
        except Exception:
            date2 = ""
        data = (str(i['questionTitle'].replace('<xmp>', "").replace('</xmp>', "").replace('<xmp>', "")),
                str(op_list), date2,
                i['answer'].replace('<xmp>', "").replace('</xmp>', "").replace('<xmp>', ""))
        c.execute("insert into  qus_bank values (?,?,?,?)", data)
        # lo=c.execute("select * from question_bank where question_text=?",data[0])
        # print(len(lo))
        conn.commit()
    return "success"
