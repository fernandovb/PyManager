# -*- coding: utf-8 -*-

import wx as wx
import wx.xrc
from os import system
from wx.lib.pubsub import pub
from _view.sys.telas.tmn01 import TMN01
from _view.sys.sulog import SULOG
from _view.sys.mn02 import MN02
from _view.sys.teste import TESTE
from _view.sys.srusr import SRUSR
from _view.sys.srcfg import SRCFG


class MN01(TMN01):

    def __init__(self, *args, **kwargs):
        super(MN01, self).__init__(*args, **kwargs)
        # Cria Barra de Status
        self.StbMenu = self.CreateStatusBar(4, wx.STB_DEFAULT_STYLE, wx.ID_ANY)
        self.StbMenu.SetStatusWidths([400, 300, 300, 300])
        self.StbMenu.SetStatusText(f'Usuário:', 1)
        self.StbMenu.SetStatusText(f'Empresa: ', 2)
        self.StbMenu.SetStatusText(f'Status da conexão: OFF', 3)
        # Cria painel menu
        self.menu = MN02(self.sb_transaction)
        self.sb_transaction.ShowNewPage(self.menu)
        # Carrega tela de login
        pub.subscribe(self.my_listener, 'frameListener')
        dlg = SULOG()
        dlg.ShowModal()

    def ac_chama_transacao(self, transacao=''):
        # t = '_view.sys.' + transacao.lower() + '.' + transacao.upper()
        if self.tc_executar.Value is not None:
            if self.sb_transaction.GetPageCount() <= 1:
                t = transacao.upper()
                try:
                    try:
                        pub.subscribe(self.my_panel, 'framePanel')
                        exec('self.panel = ' + t + '(self.sb_transaction)')
                        self.tc_executar.Value = ''
                    except:
                        pass
                    finally:
                        self.sb_transaction.ShowNewPage(self.panel)
                        self.sb_transaction.SetSelection(1)
                except:
                    self.StbMenu.SetStatusText(f'Transação "{t}" não localizada.')
                    self.mn_timer.Start(5000) # Ativa o timer para limpar a mensagem
            else:
                self.StbMenu.SetStatusText('Já existe uma seção em andamento')
                self.mn_timer.Start(5000)
    
    def ac_config(self, event):
        pass

    def on_exit(self, event):
        if self.sb_transaction.GetPageCount() > 1:
            try:
                self.sb_transaction.SetSelection(0)
                self.sb_transaction.RemovePage(1)
                self.panel.Destroy()
            except:
                pass
        else:
            dlg = wx.MessageDialog(self, "Deseja encerrar o sistema?", "Fechar sistema", style=wx.YES_NO)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_YES:
                exit()
    
    def on_keydown(self, event):
        keycode = event.GetKeyCode()
        if keycode == 13: # Verifica se a tecla <Enter> foi pressionada
            self.ac_chama_transacao(transacao=self.tc_executar.Value)
        elif keycode == 27: # Verifica se a tecla <ESC> foi pressionada
            self.tc_executar.Value = ''
        event.Skip()

    def ac_run(self, event):
        self.ac_chama_transacao(transacao=self.tc_executar.Value)

    def on_ok(self, event):
        self.panel.on_ok(event)

    def on_cancel(self, event):
        self.panel.on_cancel()

    def on_timer(self, event):
        self.StbMenu.SetStatusText('')

    def my_listener(self, message, arg2=None):
        self.Show()

    def my_panel(self, message, arg2=None):
        if message == 'close':
            self.sb_transaction.SetSelection(0)
