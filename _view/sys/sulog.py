# -*- coding: utf-8 -*-

from datetime import datetime
from wx.lib.pubsub import pub
from _view.sys.telas.tsulog import TSULOG


class SULOG(TSULOG):

    def __init__(self, *args, **kwargs):
        super(SULOG, self).__init__(None, *args, *kwargs)

    def on_cancelar(self, event):
        exit()

    def on_login(self, event):
        hora = datetime.today()
        if str(self.tc_empresa.Value).isnumeric():
            pub.sendMessage('frameListener', message='show')
            self.Destroy()
        else:
            self.tb_mensagem.Value = self.tb_mensagem.Value + '\n' + \
                                     hora.strftime('%H:%M:%S: ') + \
                                     'Campo empresa deve conter apenas números.'
