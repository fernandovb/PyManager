# -*- coding: utf-8 -*-

import wx
from wx.lib.pubsub import pub
from _view.sys.telas.tmn02 import TMN02
from _control.sys.csrcfg import darkMode


class MN02(TMN02):

    def __init__(self, parent):
        super(MN02, self).__init__(parent)
        self.defaultColour = self.GetBackgroundColour()
        self.gSizer1 = wx.GridSizer(5, 8, 0, 0)
        for button_name in [['SRUSR', 'Cadastro de Usuários'], ['SRCFG', 'Configuração do Sistema']]: 
            self.btn = wx.Button(
                self.m_panel1, label=f'{button_name[0]}\n{button_name[1]}', name=button_name[0])
            self.btn.Bind(wx.EVT_BUTTON, lambda evt, temp=button_name[0]: self.OnButton(evt, temp))
            self.gSizer1.Add(self.btn, 0, wx.ALL | wx.EXPAND, 5)
        self.m_panel1.SetSizer(self.gSizer1)
        self.m_panel1.Layout()
        darkMode(self, self.defaultColour)
        pub.sendMessage('botton_off', message=0)

    def OnButton(self, Event, button_label):
        pub.sendMessage('Transações', message=button_label)
