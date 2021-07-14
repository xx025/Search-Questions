# use to this pc auto copy and search answers
import json
import os
import time

import pyperclip

USER = ""
PaSS = ""


def get_ks(quetxt):
    import os

    import requests as requests

    os.system('cls')

    data = {'questext': quetxt,
            'user': USER,
            'pass': PaSS}
    req = requests.post(url='http://172.180.7.2/souti', data=json.dumps(data))
    req_data = req.json()
    print('''
{}
================================================
您的ip:{}\t搜索次数:{}\t最多允许搜索次数:{}
'''.format(req_data['anstext'], req_data['ipco'][0], req_data['ipco'][1], req_data['max_search']))
    return "{}".format(req_data['anstext'])


def COpyPA():
    per_copy = ""
    while True:
        copy = pyperclip.paste()
        if copy != per_copy:
            data = get_ks(copy)
            pyperclip.copy(data)
            per_copy = data
        time.sleep(0.2)


if __name__ == '__main__':
    USER = 'admin'
    PaSS = 'admin4455'

    COpyPA()
os.system("pause")
