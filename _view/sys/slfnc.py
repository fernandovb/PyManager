# -*- coding: utf-8 -*-

from wx.lib.pubsub import pub
from _view.sys.telas.tslfnc import TSLFNC


class SLFNC(TSLFNC):

    def __init__(self, parent):
        super(SLFNC, self).__init__(parent)
        funcao = ''
    
    def ac_localizar(self, event):
        if self.bt_localizar.Label == 'Localizar':
            self.bt_localizar.Label = 'Preencher'
            self.pn_lista.Show()
            self.pn_dados.Hide()
            self.bt_confirmar.Enable(True)
            self.fc_busca()
        else:
            self.bt_localizar.Label = 'Localizar'
            self.bt_confirmar.Enable(False)
            self.pn_lista.Hide()
            self.pn_dados.Show()

    def ac_selecionar(self, event):
        self.funcao = str(self.gd_resultado.GetCellValue(self.gd_resultado.GetGridCursorRow(), 0))

    def fc_busca(self):
        if self.gd_resultado.GetNumberRows() > 0:
            self.fc_limpa_tabela()
        # busca = REFOPR(self.tc_codigo.Value,
        #                self.tc_descricao.Value)
        # dados = busca.fc_buscar()
        # if dados is not None:
        #     line = 0
        #     for i in dados:
        #         self.gd_resultado.AppendRows(1)
        #         self.gd_resultado.SetCellValue(line, 0, str(i[0]))
        #         self.gd_resultado.SetCellValue(line, 1, str(i[1]))
        #         line += 1

    def fc_limpa_tabela(self):
        for i in range(self.gd_resultado.GetNumberRows()):
            self.gd_resultado.DeleteRows()
