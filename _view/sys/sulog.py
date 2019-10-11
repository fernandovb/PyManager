# -*- coding: utf-8 -*-

from datetime import datetime
from wx.lib.pubsub import pub
from _view.sys.telas.tsulog import TSULOG
from _control.sys.csulog import CSULOG


class SULOG(TSULOG):

    def __init__(self, *args, **kwargs):
        super(SULOG, self).__init__(None, *args, *kwargs)

    def on_cancelar(self, event):
        exit()

    def on_login(self, event):
        hora = datetime.today()
        if str(self.tc_empresa.Value).isnumeric():
            login = CSULOG(user=self.tc_user.Value, pw=self.tc_senha.Value)
            login.on_connection()
            if login.status:
                pub.sendMessage('frameListener', message='show', name_user=login.name_user)
                self.Destroy()
            else:
                self.tb_mensagem.Value = self.tb_mensagem.Value + '\n' + hora.strftime('%H:%M:%S: ') + login.mensagem
        else:
            self.tb_mensagem.Value = self.tb_mensagem.Value + '\n' + hora.strftime('%H:%M:%S: ') + 'Campo empresa deve conter apenas números.'
