# -*- coding: utf-8 -*-

from wx.lib.pubsub import pub
from _view.seb.telas.terncm import TERNCM
from datetime import datetime, timedelta
from dateutil.parser import parse

class ERNCM(TERNCM):

    def __init__(self, parent):
        super(ERNCM, self).__init__(parent)
        pub.sendMessage('botton_off', message=1)

    def on_ok(self):
        pass

    def on_cancel(self):
        pub.sendMessage('botton_off', message=1)
        self.messenger(mensagem='Campos limpos, sem gravar dados.')

    