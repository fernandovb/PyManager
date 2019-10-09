# -*- coding: utf-8 -*-

import _model.sys.global_conn as gconn


class MSULOG:

    def __init__(self, user, pw, host='127.0.0.1', db='E:/PyManager/database/CONTABIL.fdb'):
        self.user = user
        self.pw = pw
        self.host = host
        self.db = db
        self.connected = gconn.conn.__engine__(user=self.user, pw=self.pw, host='127.0.0.1', db='E:/PyManager/database/CONTABIL.fdb')
