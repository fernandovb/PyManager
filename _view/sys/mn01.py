# -*- coding: utf-8 -*-

import wx as wx
import wx.xrc
from os import system
from wx.lib.pubsub import pub
from _view.sys.telas.tmn01 import TMN01
from _view.sys.sulog import SULOG
from _view.sys.mn02 import MN02
from _view.sys.srusr import SRUSR
from _view.sys.srcfg import SRCFG
from _control.sys.csrcfg import darkMode
import _model.sys.global_conn as gconn


class MN01(TMN01):

    def __init__(self, *args, **kwargs):
        super(MN01, self).__init__(*args, **kwargs)
        self.defaultColour = self.GetBackgroundColour()
        darkMode(self, self.defaultColour)

        # Cria Barra de Status
        self.StbMenu = self.CreateStatusBar(4, wx.STB_DEFAULT_STYLE, wx.ID_ANY)
        self.StbMenu.SetStatusWidths([400, 300, 300, 300])
        self.StbMenu.SetStatusText(f'Usuário:', 1)
        self.StbMenu.SetStatusText(f'Empresa: ', 2)
        self.StbMenu.SetStatusText(f'Status da conexão: OFF', 3)
        # Cria mensageiros
        pub.subscribe(self.messenger, 'Messenger')
        pub.subscribe(self.transaction, 'Transações')
        pub.subscribe(self.botton_off, 'botton_off')
        # Carrega tela de login
        pub.subscribe(self.my_listener, 'frameListener')
        dlg = SULOG()
        dlg.ShowModal()
        # Cria painel menu
        self.menu = MN02(self.sb_transaction)
        self.sb_transaction.ShowNewPage(self.menu)
        self.list_transaction = ['SRUSR', 'SRCFG']

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
                    self.StbMenu.SetStatusText(
                        f'Transação "{t}" não localizada.')
                    # Ativa o timer para limpar a mensagem
                    self.mn_timer.Start(5000)
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
                self.panel.on_close()
            except:
                pass
        else:
            dlg = wx.MessageDialog(
                self, "Deseja encerrar o sistema?", "Fechar sistema", style=wx.YES_NO)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_YES:
                gconn.conn.close_connection()
                wx.Exit()

    def on_keydown(self, event):
        keycode = event.GetKeyCode()
        if keycode == 13:  # Verifica se a tecla <Enter> foi pressionada
            self.ac_chama_transacao(transacao=self.tc_executar.Value)
        elif keycode == 27:  # Verifica se a tecla <ESC> foi pressionada
            self.tc_executar.Value = ''
        event.Skip()

    def ac_run(self, event):
        self.ac_chama_transacao(transacao=self.tc_executar.Value)

    def on_ok(self, event):
        self.panel.on_ok()

    def on_cancel(self, event):
        self.panel.on_cancel()

    def on_find(self, event):
        self.panel.on_find()

    def on_timer(self, event):
        self.StbMenu.SetStatusText('')

    def on_insert(self, event):
        self.panel.on_insert()

    def on_edit(self, event):
        self.panel.on_edit()

    def on_delete(self, event):
        pass

    def on_print(self, event):
        pass

    def on_pdf(self, event):
        pass

    def my_listener(self, message, name_user, arg2=None):
        if not gconn.conn.user == None:
            self.StbMenu.SetStatusText(f'Usuário: {name_user}', 1)
            self.StbMenu.SetStatusText(f'Empresa: {gconn.conn.db}', 2)
            self.StbMenu.SetStatusText('Status da conexão: ON', 3)
        self.Show()

    def my_panel(self, message, arg2=None):
        if message == 'close':
            self.sb_transaction.SetSelection(0)
        else:
            self.StbMenu.SetStatusText(message)

    def messenger(self, message, arg2=None):
        self.StbMenu.SetStatusText(message)
        self.mn_timer.Start(5000)

    def transaction(self, message, arg2=None):
        if message in self.list_transaction:
            self.ac_chama_transacao(transacao=message)

    def botton_off(self, message, arg2=None):
        if message == 0:
            # Desabilita botões - Menu em Exibição
            self.tb_mn01.EnableTool(wx.ID_SAVE, False)
            self.tb_mn01.EnableTool(wx.ID_CANCEL, False)
            self.tb_mn01.EnableTool(wx.ID_FIND, False)
            self.tb_mn01.EnableTool(wx.ID_ADD, False)
            self.tb_mn01.EnableTool(wx.ID_EDIT, False)
            self.tb_mn01.EnableTool(wx.ID_DELETE, False)
            self.tb_mn01.EnableTool(wx.ID_PRINT, False)
        elif message == 1:
            # Habilita botões - Tela sem dados
            self.tb_mn01.EnableTool(wx.ID_SAVE, False)
            self.tb_mn01.EnableTool(wx.ID_CANCEL, False)
            self.tb_mn01.EnableTool(wx.ID_FIND, True)
            self.tb_mn01.EnableTool(wx.ID_ADD, True)
            self.tb_mn01.EnableTool(wx.ID_EDIT, False)
            self.tb_mn01.EnableTool(wx.ID_DELETE, False)
            self.tb_mn01.EnableTool(wx.ID_PRINT, False)
        elif message == 2:
            # Habilita botões - Tela com dados sem edição
            self.tb_mn01.EnableTool(wx.ID_SAVE, False)
            self.tb_mn01.EnableTool(wx.ID_CANCEL, False)
            self.tb_mn01.EnableTool(wx.ID_FIND, True)
            self.tb_mn01.EnableTool(wx.ID_ADD, True)
            self.tb_mn01.EnableTool(wx.ID_EDIT, True)
            self.tb_mn01.EnableTool(wx.ID_DELETE, True)
            self.tb_mn01.EnableTool(wx.ID_PRINT, False)
        elif message == 3:
            # Habilita botões - Tela com dados em edição
            self.tb_mn01.EnableTool(wx.ID_SAVE, True)
            self.tb_mn01.EnableTool(wx.ID_CANCEL, True)
            self.tb_mn01.EnableTool(wx.ID_FIND, False)
            self.tb_mn01.EnableTool(wx.ID_ADD, False)
            self.tb_mn01.EnableTool(wx.ID_EDIT, False)
            self.tb_mn01.EnableTool(wx.ID_DELETE, False)
            self.tb_mn01.EnableTool(wx.ID_PRINT, False)
