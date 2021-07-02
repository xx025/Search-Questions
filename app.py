import json
import sqlite3
from random import random

from flask import Flask, send_from_directory
from flask import request, jsonify, render_template, redirect, url_for, session, g
from flask_cors import CORS

import setting
from pyscript import QuestionBank
from pyscript.SQLitesjdbc import db_con
from pyscript.SearchAns import searchAns
from pyscript.add_ques_to_qdb import add_ques

app = Flask(__name__, static_folder=setting.setting.static_floder, template_folder=setting.setting.template_folder)
app.secret_key = '^\x90\xcd-N\xc2:z\xee\xfckHOUjy\xe0\x83b\x12\x1f\xe3Wb' + str(random())
CORS(app, resources=r'/*')
CORS(app, supports_credentials=True)
max_search = setting.setting.max_search

qkn = QuestionBank.ques_bank()
qb = qkn.get_ques_bank()

from flask import current_app


@app.route('/favicon.ico')
def get_fav():
    return current_app.send_static_file('static/favicon.ico')


@app.teardown_appcontext
def close_connection(exc):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/download")
def index():
    c = db_con()
    c.behavior_log((request.remote_addr, session.get('username'), '下载', ""))
    return send_from_directory(directory=setting.setting.static_floder, path="main_question_bank.csv",
                               as_attachment=True)


@app.route('/login', methods=['post', 'get'])
def login():
    c = db_con()
    if request.method == 'POST':
        student = request.data.decode('utf-8')
        student = json.loads(student)
        if c.isacount(student['user'], student['pass']):
            session['username'] = student['user']
            c.behavior_log((request.remote_addr, session.get('username'), '登录', ''))
            return {"url": "/"}

    return render_template('login.html')


@app.route('/')
def success():
    if session.get('username') is not None:
        c = db_con()
        data = c.query(request.remote_addr)
        return render_template('search.html', ip=data[0], count=data[1], name=session.get('username'),
                               max_search=max_search)
    return redirect(url_for('login'))


@app.route('/souti', methods=['post', 'get'])
def query_ques():
    if not request.data:  # 检测是否有数据
        return 'fail'
    else:
        # 两种情况
        c = db_con()
        student = request.data.decode('utf-8')
        student_json = json.loads(student)  # return x:dict()
        user_name = ""
        sw_k = 0
        if 'user' in student_json and 'pass' in student_json:
            if c.isacount(student_json['user'], student_json['pass']):
                login = True
                user_name = student_json['user']
            else:
                sw_k = 1
                login = False
        else:
            if session.get('username') is not None:
                login = True
                user_name = session.get('username')
            else:
                login = False
                sw_k = 2
    data = c.query(user=user_name)
    if login:
        if data[1] < max_search:
            c.add(session.get('username'))
            ans = searchAns(student_json['questext']).basecover(ques_bank=qb)
            c.behavior_log((request.remote_addr, user_name, '搜题', student_json['questext']))
            student_json["anstext"] = ans.get_self_str()
            student_json["ipco"] = (request.remote_addr,data[1])
            return jsonify(student_json)
        else:
            return jsonify({"anstext": "次数受限", "ipco": data})
    else:
        if sw_k == 1:
            return jsonify({"anstext": "请检查账户", "ipco": data})
        if sw_k == 2:
            return jsonify({"anstext": "请刷新网页", "ipco": data})


@app.route("/add_ques", methods=['GET', 'POST'])
def add_ques():
    if not request.data:  # 检测是否有数据
        return 'fail'
    else:
        return add_ques()



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
