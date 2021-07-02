# -*- coding:utf8 -*-
from configparser import ConfigParser


class config():
    sqlite_db = str()
    question_bank = str()
    max_search = 0
    av_code = False
    static_floder = str()
    template_folder = str()

    def __init__(self):
        cp = ConfigParser()
        # 以.cfg结尾的配置文件
        cp.read('config.cfg', encoding='utf8')
        # 以.ini结尾的配置文件
        # cp.read("config.ini")
        path_root = cp.get('path_root', 'path')
        self.sqlite_db = path_root + cp.get('sqlite_db', 'path')
        self.question_bank = path_root + cp.get('question_bank', 'path')
        self.max_search = int(cp.get('webserver', 'max_search'))
        self.template_folder = path_root + cp.get('webserver', 'template_folder')
        self.static_floder = path_root + cp.get('webserver', 'static_floder')
        self.av_code = bool(cp.get('pc', 'av_code'))


setting = config()
