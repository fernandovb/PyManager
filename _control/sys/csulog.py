# -*- coding: utf-8 -*-

from _model.sys.msulog import MSULOG
from _model.sys.msrusr import MSRUSR


class CSULOG:

    def __init__(self, user='sysdba', pw='masterkey', host='127.0.0.1', db='E:/PyManager/database/CONTABIL.fdb'):
        self.user = user.upper()
        self.pw = pw
        self.host = host
        self.db = db
        self.name_user = None
    
    def on_connection(self):
        login = MSULOG(user=self.user, pw=self.pw)
        usuario = MSRUSR()
        data_user = usuario.find_user(user=self.user)
        self.name_user = data_user.nome_usuario
        self.status = login.connected[0]
        self.mensagem = login.connected[1]
 