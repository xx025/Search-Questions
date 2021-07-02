import hashlib
import sqlite3
from datetime import datetime

from flask import g

import setting

DATABASE = setting.setting.sqlite_db


class db_con:
    conn = None
    c = None

    def __init__(self):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        self.conn = db
        self.c = self.conn.cursor()

    def query(self, user: str):
        corsor = self.c.execute("select * from search_count where user=:user ", {"user": user})
        re = list(corsor)
        if len(re) == 0:
            self.insert(user=user)
            return user, 0
        else:
            return re[0]

    def insert(self, user: str):
        self.c.execute("insert into search_count values (:user,:count )", {"user": user, "count": 0})
        self.conn.commit()

    def add(self, user):
        data = self.query(user=user)
        data = (data[1] + 1, data[0])
        self.c.execute("UPDATE search_count set count=?where user=?", data)
        self.conn.commit()
        return self.query(user=user)

    def isacount(self, username: str, password: str):
        user = hashlib.sha256(username.encode('utf-8')).hexdigest()
        pass2 = hashlib.sha256(password.encode('utf-8')).hexdigest()
        corsor = self.c.execute("select * from users where user =? and pass= ?", (user, pass2))
        if len(list(corsor)) == 0:
            return False
        else:
            return True

    def behavior_log(self, data: tuple):
        self.c.execute("insert into  behavior_log values (?,?,?,?,?)", data + (datetime.now(),))
        self.conn.commit()

    def insert_ques(self, data):
        self.c.execute("insert into  question_bank values (?,?,?,?,?)", data)
        self.conn.commit()

    def get_ques(self):
        self.c.execute("select * from question_bank")
