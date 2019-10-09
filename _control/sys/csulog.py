# -*- coding: utf-8 -*-

from _model.sys.msulog import MSULOG


class CSULOG:

    def __init__(self, user='sysdba', pw='masterkey', host='127.0.0.1', db='E:/PyManager/database/CONTABIL.fdb'):
        self.user = user
        self.pw = pw
        self.host = host
        self.db = db
    
    def on_connection(self):
        login = MSULOG(user=self.user, pw=self.pw)
        self.status = login.connected[0]
        self.mensagem = login.connected[1]
 