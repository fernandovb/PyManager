# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
# Class TERNCM
###########################################################################


class TERNCM (wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(559, 377), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos,
                          size=size, style=style, name=name)

        lay_body = wx.BoxSizer(wx.VERTICAL)

        lay_title = wx.BoxSizer(wx.HORIZONTAL)

        self.pn_title = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        lay_data_title = wx.BoxSizer(wx.HORIZONTAL)

        self.lb_transaction_name1 = wx.StaticText(
            self.pn_title, wx.ID_ANY, u"Cadastro de NCM/SH", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lb_transaction_name1.Wrap(-1)

        self.lb_transaction_name1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(
        ), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tahoma"))

        lay_data_title.Add(self.lb_transaction_name1, 1, wx.ALL, 5)

        self.lb_transaction_code1 = wx.StaticText(
            self.pn_title, wx.ID_ANY, u"ERNCM", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lb_transaction_code1.Wrap(-1)

        self.lb_transaction_code1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(
        ), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tahoma"))

        lay_data_title.Add(self.lb_transaction_code1, 0, wx.ALL, 5)

        self.pn_title.SetSizer(lay_data_title)
        self.pn_title.Layout()
        lay_data_title.Fit(self.pn_title)
        lay_title.Add(self.pn_title, 1, wx.ALL | wx.EXPAND, 1)

        lay_body.Add(lay_title, 0, wx.ALIGN_TOP | wx.EXPAND, 0)

        lay_widgets = wx.BoxSizer(wx.VERTICAL)

        self.sb_widgets = wx.Simplebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE)
        self.pn_data_fields = wx.Panel(
            self.sb_widgets, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE)
        lay_dispenser = wx.BoxSizer(wx.HORIZONTAL)

        lay_label_1 = wx.BoxSizer(wx.VERTICAL)

        self.lb_ncm = wx.StaticText(self.pn_data_fields, wx.ID_ANY,
                                    u"NCM/SH:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lb_ncm.Wrap(-1)

        self.lb_ncm.SetMinSize(wx.Size(100, 25))

        lay_label_1.Add(self.lb_ncm, 0, wx.ALL, 2)

        self.lb_capitulo = wx.StaticText(
            self.pn_data_fields, wx.ID_ANY, u"Capítulo:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lb_capitulo.Wrap(-1)

        self.lb_capitulo.SetMinSize(wx.Size(100, 25))

        lay_label_1.Add(self.lb_capitulo, 0, wx.ALL, 2)

        self.lb_descricao = wx.StaticText(
            self.pn_data_fields, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lb_descricao.Wrap(-1)

        self.lb_descricao.SetMinSize(wx.Size(100, 25))

        lay_label_1.Add(self.lb_descricao, 0, wx.ALL, 2)

        self.lb_vigencia_ini = wx.StaticText(
            self.pn_data_fields, wx.ID_ANY, u"Vig.inicial:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lb_vigencia_ini.Wrap(-1)

        self.lb_vigencia_ini.SetMinSize(wx.Size(100, 25))

        lay_label_1.Add(self.lb_vigencia_ini, 0, wx.ALL, 5)

        self.lb_vigencia_fim = wx.StaticText(
            self.pn_data_fields, wx.ID_ANY, u"Vig.fim:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lb_vigencia_fim.Wrap(-1)

        self.lb_vigencia_fim.SetMinSize(wx.Size(100, 25))

        lay_label_1.Add(self.lb_vigencia_fim, 0, wx.ALL, 2)

        self.lb_umd = wx.StaticText(self.pn_data_fields, wx.ID_ANY,
                                    u"Un. Medida:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lb_umd.Wrap(-1)

        self.lb_umd.SetMinSize(wx.Size(100, 25))

        lay_label_1.Add(self.lb_umd, 0, wx.ALL, 2)

        lay_dispenser.Add(lay_label_1, 0, wx.EXPAND, 5)

        lay_text_1 = wx.BoxSizer(wx.VERTICAL)

        self.tc_ncm = wx.TextCtrl(self.pn_data_fields, wx.ID_ANY,
                                  wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 25), 0)
        self.tc_ncm.SetMaxLength(8)
        lay_text_1.Add(self.tc_ncm, 0, wx.ALL, 2)

        self.tc_capitulo = wx.TextCtrl(
            self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(35, 25), 0)
        self.tc_capitulo.SetMaxLength(2)
        lay_text_1.Add(self.tc_capitulo, 0, wx.ALL, 2)

        self.tc_descricao = wx.TextCtrl(
            self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, 25), 0)
        self.tc_descricao.SetMaxLength(500)
        lay_text_1.Add(self.tc_descricao, 0, wx.ALL, 2)

        self.tc_vigencia_ini = wx.TextCtrl(
            self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 25), 0)
        lay_text_1.Add(self.tc_vigencia_ini, 0, wx.ALL, 2)

        self.tc_vigencia_fim = wx.TextCtrl(
            self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 25), 0)
        lay_text_1.Add(self.tc_vigencia_fim, 0, wx.ALL, 2)

        self.tc_umd = wx.TextCtrl(self.pn_data_fields, wx.ID_ANY,
                                  wx.EmptyString, wx.DefaultPosition, wx.Size(40, 25), 0)
        lay_text_1.Add(self.tc_umd, 0, wx.ALL, 2)

        lay_dispenser.Add(lay_text_1, 0, wx.EXPAND, 1)

        self.pn_data_fields.SetSizer(lay_dispenser)
        self.pn_data_fields.Layout()
        lay_dispenser.Fit(self.pn_data_fields)
        self.sb_widgets.AddPage(self.pn_data_fields, u"Cadastro", False)
        self.pn_data_list = wx.Panel(
            self.sb_widgets, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE)
        lay_grid_list = wx.BoxSizer(wx.VERTICAL)

        self.mg_search = wx.grid.Grid(
            self.pn_data_list, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.mg_search.CreateGrid(1, 6)
        self.mg_search.EnableEditing(True)
        self.mg_search.EnableGridLines(True)
        self.mg_search.EnableDragGridSize(False)
        self.mg_search.SetMargins(0, 0)

        # Columns
        self.mg_search.SetColSize(0, 100)
        self.mg_search.SetColSize(1, 70)
        self.mg_search.SetColSize(2, 400)
        self.mg_search.SetColSize(3, 100)
        self.mg_search.SetColSize(4, 100)
        self.mg_search.SetColSize(5, 50)
        self.mg_search.EnableDragColMove(False)
        self.mg_search.EnableDragColSize(True)
        self.mg_search.SetColLabelSize(30)
        self.mg_search.SetColLabelValue(0, u"NCM/SH")
        self.mg_search.SetColLabelValue(1, u"Capítulo")
        self.mg_search.SetColLabelValue(2, u"Descrição")
        self.mg_search.SetColLabelValue(3, u"Vig.Inicial")
        self.mg_search.SetColLabelValue(4, u"Vig.Final")
        self.mg_search.SetColLabelValue(5, u"UMD")
        self.mg_search.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.mg_search.EnableDragRowSize(True)
        self.mg_search.SetRowLabelSize(30)
        self.mg_search.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.mg_search.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        lay_grid_list.Add(self.mg_search, 1, wx.EXPAND, 5)

        self.pn_data_list.SetSizer(lay_grid_list)
        self.pn_data_list.Layout()
        lay_grid_list.Fit(self.pn_data_list)
        self.sb_widgets.AddPage(self.pn_data_list, u"Lista", False)

        lay_widgets.Add(self.sb_widgets, 1, wx.EXPAND | wx.ALL, 0)

        lay_body.Add(lay_widgets, 1, wx.EXPAND, 5)

        lay_botton = wx.BoxSizer(wx.HORIZONTAL)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.bt_search = wx.Button(
            self, wx.ID_ANY, u"Localizar", wx.DefaultPosition, wx.Size(100, 36), 0)

        self.bt_search.SetBitmap(
            wx.Bitmap(u"desingner/icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY))
        self.bt_search.SetBitmapDisabled(
            wx.Bitmap(u"desingner/icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY))
        bSizer7.Add(self.bt_search, 0, wx.ALL, 5)

        self.bt_import = wx.Button(
            self, wx.ID_ANY, u"&Importar Tabela", wx.DefaultPosition, wx.Size(-1, 36), 0)
        bSizer7.Add(self.bt_import, 0, wx.ALL, 5)

        bSizer7.Add((0, 0), 1, wx.EXPAND, 0)

        lay_botton.Add(bSizer7, 1, wx.EXPAND, 5)

        lay_body.Add(lay_botton, 0, wx.ALIGN_BOTTOM | wx.EXPAND, 0)

        self.SetSizer(lay_body)
        self.Layout()

        # Connect Events
        self.tc_umd.Bind(wx.EVT_KILL_FOCUS, self.on_kill_focus)
        self.mg_search.Bind(
            wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_grid_dclick)
        self.bt_search.Bind(wx.EVT_BUTTON, self.ac_search)
        self.bt_import.Bind(wx.EVT_BUTTON, self.on_import)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_kill_focus(self, event):
        event.Skip()

    def on_grid_dclick(self, event):
        event.Skip()

    def ac_search(self, event):
        event.Skip()

    def on_import(self, event):
        event.Skip()
