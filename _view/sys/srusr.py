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
        self.bt_search.SetFocus()
        pub.sendMessage('botton_off', message=1)
        self.ac_libera_campos(ativa=False)

    def on_ok(self):
        self.data_save()
    
    def on_cancel(self):
        self.messenger(mensagem='Campos limpos, sem gravar dados.')
        self.tc_clear()
    
    def on_insert(self):
        pub.sendMessage('botton_off', message=3)
        self.tc_clear()
        self.ac_libera_campos(ativa=True)

    def on_edit(self):
        pub.sendMessage('botton_off', message=3)
        self.ac_libera_campos(ativa=True)

    def on_delete(self):
        pass

    def on_print(self):
        pass

    def on_pdf(self):
        pass

    def on_close(self):
        self.messenger(mensagem='Transação encerrada!')
        pub.sendMessage('botton_off', message=0)
        pub.sendMessage('framePanel', message='close')
        self.Destroy()
    
    def on_find(self):
        if self.sb_widgets.GetSelection() == 0:
            try:
                consulta = CSRUSR(id_matricula=self.tc_matricula.Value)
                consulta.search_records()
                self.tc_matricula.Value = str(consulta.id_matricula)
                self.cb_situacao.SetSelection(consulta.situacao)
                self.tc_nome.Value = str(consulta.nome_usuario)
                self.tc_setor.Value = str(consulta.id_setor)
                self.tc_funcao.Value = str(consulta.id_funcao)
                self.tc_senha.Value = str(consulta.senha)
                self.tc_frequencia.Value = str(consulta.frequencia)
                if self.tc_frequencia.Value != '':
                    self.tc_vigencia.Value = self.calc_date()
                pub.sendMessage('botton_off', message=2)
            except:
                pass
        elif self.sb_widgets.GetSelection() == 1:
            try:
                for i in range(self.mg_search.GetNumberRows()):
                    self.mg_search.DeleteRows()
                consulta = CSRUSR(id_matricula='')
                lista = consulta.search_all_records()
                line = 0
                for record in lista:
                    self.mg_search.AppendRows(1)
                    self.mg_search.SetCellValue(line, 0, str(record.id_matricula))
                    self.mg_search.SetCellValue(line, 1, str(record.nome_usuario))
                    line += 1
                self.mg_search.EnableEditing(False)
            except:
                pass

    def messenger(self, mensagem=''):
        pub.sendMessage('Messenger', message=mensagem)

    def on_kill_focus(self, event):
        if self.tc_frequencia.Value != '':
            self.tc_vigencia.Value = self.calc_date()
        event.Skip()

    def calc_date(self):
        vigencia = datetime.today() + timedelta(days=float(self.tc_frequencia.Value))
        return vigencia.strftime('%d/%m/%Y')

    def ac_search(self, event):
        if self.bt_search.Label == 'Localizar':
            self.sb_widgets.SetSelection(1)
            self.bt_search.Label = 'Retornar'
            self.bt_select.Show()
        else:
            self.sb_widgets.SetSelection(0)
            self.bt_search.Label = 'Localizar'
            self.bt_select.Hide()
    
    def on_grid_dclick(self, event):
        linha = self.mg_search.GetGridCursorRow()
        matricula = self.mg_search.GetCellValue(linha, 0)
        try:
            consulta = CSRUSR(id_matricula=matricula)
            consulta.search_records()
            self.tc_matricula.Value = str(consulta.id_matricula)
            self.cb_situacao.SetSelection(consulta.situacao)
            self.tc_nome.Value = str(consulta.nome_usuario)
            self.tc_setor.Value = str(consulta.id_setor)
            self.tc_funcao.Value = str(consulta.id_funcao)
            self.tc_senha.Value = str(consulta.senha)
            self.tc_frequencia.Value = str(consulta.frequencia)
            if self.tc_frequencia.Value != '':
                self.tc_vigencia.Value = self.calc_date()
            pub.sendMessage('botton_off', message=2)
        except:
            pass
        self.sb_widgets.SetSelection(0)
        self.bt_search.Label = 'Localizar'
        self.bt_select.Hide()

    def on_reset_pass(self, event):
        pass

    def data_save(self):
        font = CSRUSR(self.tc_matricula.Value, 
                        self.cb_situacao.GetSelection(),
                        self.tc_nome.Value,
                        self.tc_setor.Value,
                        self.tc_funcao.Value,
                        self.tc_senha.Value,
                        self.cb_redefinir.Value,
                        self.tc_frequencia.Value)
        font.ac_insert()
        self.messenger(mensagem='Dados gravados.')
        self.tc_clear()
    
    def tc_clear(self):
        if self.sb_widgets.GetSelection() == 0:
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
        elif self.sb_widgets.GetSelection() == 1:
            for i in range(self.mg_search.GetNumberRows()):
                self.mg_search.DeleteRows()
            self.mg_search.AppendRows(1)
            self.mg_search.EnableEditing(True)
    
    def ac_libera_campos(self, ativa=False):
        self.cb_situacao.Enable(ativa)
        self.tc_nome.Enable(ativa)
        self.tc_setor.Enable(ativa)
        self.bt_fd_setor.Enable(ativa)
        self.tc_funcao.Enable(ativa)
        self.bt_fd_funcao.Enable(ativa)
        self.cb_redefinir.Enable(ativa)
        self.tc_senha.Enable(ativa)
        self.tc_vigencia.Enable(ativa)
        self.tc_frequencia.Enable(ativa)
