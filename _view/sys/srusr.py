# -*- coding: utf-8 -*-

from wx.lib.pubsub import pub
from _view.sys.telas.tsrusr import TSRUSR
from _control.sys.csrusr import CSRUSR
from datetime import datetime, timedelta
from dateutil.parser import parse


class SRUSR(TSRUSR):

    def __init__(self, parent):
        super(SRUSR, self).__init__(parent)
        self.data_list = []
        self.bt_find.SetFocus()

    def on_ok(self):
        self.data_save()
    
    def on_cancel(self):
        self.tc_clear()

    def on_close(self):
        pub.sendMessage('framePanel', message='close')
        self.Destroy()

    def on_kill_focus(self, event):
        now = datetime.today()
        if self.tc_frequencia.Value != '':
            vigencia = datetime.today() + timedelta(days=float(self.tc_frequencia.Value))
            self.tc_vigencia.Value = vigencia.strftime('%d/%m/%Y')
        event.Skip()
    
    def ac_find(self, event):
        if self.bt_find.Label == 'Localizar':
            self.sb_widgets.SetSelection(1)
            self.bt_find.Label = 'Buscar'
        else:
            self.sb_widgets.SetSelection(0)
            self.bt_find.Label = 'Localizar'

    def on_reset_pass(self, event):
        pass

    def data_save(self):
        font = CSRUSR(self.tc_matricula.Value, 
                    self.cb_situacao.Value, 
                    self.tc_nome.Value, 
                    self.tc_setor.Value, 
                    self.tc_funcao.Value, 
                    self.tc_senha.Value)
        self.data_list.append(font)
        self.tc_clear()
    
    def tc_clear(self):
        self.tc_matricula.Value = ''
        self.cb_situacao.Selection = -1
        self.tc_nome.Value = ''
        self.tc_setor.Value = ''
        self.lb_nome_setor.Label = ''
        self.tc_funcao.Value = ''
        self.cb_redefinir.Value = False
        self.tc_senha.Value = ''
        self.tc_vigencia.Value = ''
        self.tc_frequencia.Value = ''
