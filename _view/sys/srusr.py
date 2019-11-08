# -*- coding: utf-8 -*-

from wx.lib.pubsub import pub
from _view.sys.telas.tsrusr import TSRUSR
from _view.sys.slfnc import SLFNC
from _control.sys.csrusr import CSRUSR, Error
from _control.sys.csrcfg import darkMode
from datetime import datetime, timedelta
from dateutil.parser import parse


class SRUSR(TSRUSR):

    def __init__(self, parent):
        super(SRUSR, self).__init__(parent)
        self.defaultColour = self.GetBackgroundColour()
        darkMode(self.sb_widgets, self.defaultColour)
        darkMode(self, self.defaultColour)
        self.data_list = []
        self.bt_search.SetFocus()
        pub.sendMessage('botton_off', message=1)
        self.ac_libera_campos(ativa=False)
        self.user = None

    def on_ok(self):
        """Confirma dados para gravação
        Envia os dados informados para o banco de dados e grava as modificações.
        """
        pub.sendMessage('botton_off', message=1)
        self.data_save()
        self.ac_libera_campos()
    
    def on_cancel(self):
        """Cancela edição/inserção em andamento
        Anula as alterações feitas e inativa campos para edição
        """
        if self.tc_matricula.Value == '':
            pub.sendMessage('botton_off', message=1)
        else:
            pub.sendMessage('botton_off', message=2)
        self.up_data()
        self.ac_libera_campos(ativa=False)
        self.messenger(mensagem='Campos limpos, sem gravar dados.')
    
    def on_insert(self):
        """Cria novo registro
        Cria um objeto 'self.user' para inclusão de dados novos.
        """
        pub.sendMessage('botton_off', message=3)
        self.tc_clear()
        self.ac_libera_campos(ativa=True)
        self.tc_matricula.Enable(True)
        self.user = CSRUSR()

    def on_edit(self):
        """Altera um registro existente
        Libera os campos dos dados exibidos para edição.
        """
        pub.sendMessage('botton_off', message=3)
        self.ac_libera_campos(ativa=True)

    def on_delete(self):
        pass

    def on_print(self):
        pass

    def on_pdf(self):
        pass

    def on_close(self):
        """Encerra transação
        Fecha a transação e destroi o objeto 'wx.Panel' aberto.
        """
        self.messenger(mensagem='Transação encerrada!')
        pub.sendMessage('botton_off', message=0)
        pub.sendMessage('framePanel', message='close')
        self.Destroy()
    
    def on_find(self):
        """Localiza registro, ou registros
        Realiza consulta individual, com o preenchimento da matrícula,
        ou traz todos os usuários existentes no banco de dados.
        """
        if self.sb_widgets.GetSelection() == 0:
            try:
                self.user = CSRUSR(id_matricula=self.tc_matricula.Value)
                self.user.search_records()
                self.up_data()
                pub.sendMessage('botton_off', message=2)
            except Error as e:
                self.messenger(mensagem=e)
            except:
                self.messenger(mensagem='Erro: Erro não localizado; função: on_find(SRUSR)')
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
            self.user = CSRUSR(id_matricula=matricula)
            self.user.search_records()
            self.up_data()
            pub.sendMessage('botton_off', message=2)
        except:
            pass
        self.sb_widgets.SetSelection(0)
        self.bt_search.Label = 'Localizar'
        self.bt_select.Hide()

    def on_reset_pass(self, event):
        pass

    def ac_find_setor(self, event):
        pass

    def ac_find_funcao(self, event):
        fc = ''
        funcao = SLFNC(self)
        if funcao.ShowModal() == wx.ID_OK:
            fc = str(funcao.funcao)
        funcao.Destroy()
        return fc

    def data_save(self):
        """Salva os dados informados.
        Verifica se o objeto 'self.user' tem um matrícula, validando sua existência.
        Se tiver, atualizará os dados e fará um update,
        se não, copiará os dados para objeto e fará um insert.

        Não retorna valor. Exibe mensagem de confirmação.
        """
        try:
            if self.user.id_matricula == '':
                self.down_data()
                self.user.ac_insert()
            else:
                self.down_data()
                self.user.ac_update()
            self.messenger(mensagem='Dados gravados.')
        except Error as e:
            self.messenger(mensagem=e)
        except:
            self.messenger(mensagem='Erro ao gravar dados.')

    def up_data(self):
        """Carrega os dados do usuário ativo
        Copia as informações do objeto 'self.user' para os campos da tela.

        Não retorna dados.
        """
        self.tc_matricula.Value = str(self.user.id_matricula).upper()
        self.cb_situacao.SetSelection(self.user.situacao)
        self.tc_nome.Value = str(self.user.nome_usuario).upper()
        self.tc_setor.Value = str(self.user.id_setor)
        self.tc_funcao.Value = str(self.user.id_funcao)
        if self.user.redefinir == 0:
            self.cb_redefinir.Value = False
        else:
            self.cb_redefinir.Value = True
        self.tc_senha.Value = str(self.user.senha)
        self.tc_frequencia.Value = str(self.user.frequencia)
        if self.tc_frequencia.Value != '':
            self.tc_vigencia.Value = self.calc_date()

    def down_data(self):
        """Atualiza os dados do usuário ativo.
        Copia as informações dos campos para o objeto 'self.user'.

        Não retorna dados.
        """
        self.user.id_matricula = str(self.tc_matricula.Value).upper()
        self.user.situacao = int(self.cb_situacao.Selection)
        self.user.nome_usuario = str(self.tc_nome.Value).upper()
        self.user.id_setor = int(self.tc_setor.Value)
        self.user.id_funcao = int(self.tc_funcao.Value)
        if self.cb_redefinir.Value == False:
            self.user.redefinir = 0
        else:
            self.user.redefinir = 1
        self.user.senha = str(self.tc_senha.Value)
        self.user.frequencia = int(self.tc_frequencia.Value)

    def tc_clear(self):
        """Limpa campos
        Apaga as informações dos campos de tela.
        """
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
        """Ativa/desativa campos da tela
        Altera a liberação dos campos para edição.

        Sintaxe: ac_libera_campos(ativa=True) para ativar campos;
                 ac_libera_campos() para desativar campos.
        """
        self.tc_matricula.Enable(not ativa)
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
