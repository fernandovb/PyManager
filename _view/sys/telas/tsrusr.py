# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class TSRUSR
###########################################################################

class TSRUSR ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 559,377 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		lay_body = wx.BoxSizer( wx.VERTICAL )

		lay_title = wx.BoxSizer( wx.HORIZONTAL )

		self.pn_title = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_data_title = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_transaction_name1 = wx.StaticText( self.pn_title, wx.ID_ANY, u"Cadastro de Usuários", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_transaction_name1.Wrap( -1 )

		self.lb_transaction_name1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tahoma" ) )

		lay_data_title.Add( self.lb_transaction_name1, 1, wx.ALL, 5 )

		self.lb_transaction_code1 = wx.StaticText( self.pn_title, wx.ID_ANY, u"SRUSR", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lb_transaction_code1.Wrap( -1 )

		self.lb_transaction_code1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tahoma" ) )

		lay_data_title.Add( self.lb_transaction_code1, 0, wx.ALL, 5 )


		self.pn_title.SetSizer( lay_data_title )
		self.pn_title.Layout()
		lay_data_title.Fit( self.pn_title )
		lay_title.Add( self.pn_title, 1, wx.ALL|wx.EXPAND, 1 )


		lay_body.Add( lay_title, 0, wx.ALIGN_TOP|wx.EXPAND, 0 )

		lay_widgets = wx.BoxSizer( wx.VERTICAL )

		self.sb_widgets = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.pn_data_fields = wx.Panel( self.sb_widgets, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
		lay_dispenser = wx.BoxSizer( wx.HORIZONTAL )

		lay_label_1 = wx.BoxSizer( wx.VERTICAL )

		self.lb_matricula = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Matrícula:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lb_matricula.Wrap( -1 )

		self.lb_matricula.SetMinSize( wx.Size( 100,25 ) )

		lay_label_1.Add( self.lb_matricula, 0, wx.ALL, 2 )

		self.lb_nome = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Nome:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lb_nome.Wrap( -1 )

		self.lb_nome.SetMinSize( wx.Size( 100,25 ) )

		lay_label_1.Add( self.lb_nome, 0, wx.ALL, 2 )

		self.lb_setor = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Setor:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lb_setor.Wrap( -1 )

		self.lb_setor.SetMinSize( wx.Size( 100,25 ) )

		lay_label_1.Add( self.lb_setor, 0, wx.ALL, 2 )

		self.lb_funcao = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Função:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lb_funcao.Wrap( -1 )

		self.lb_funcao.SetMinSize( wx.Size( 100,25 ) )

		lay_label_1.Add( self.lb_funcao, 0, wx.ALL, 5 )

		self.lb_senha = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Senha:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lb_senha.Wrap( -1 )

		self.lb_senha.SetMinSize( wx.Size( 100,25 ) )

		lay_label_1.Add( self.lb_senha, 0, wx.ALL, 2 )

		self.lb_frequencia = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Frequência:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lb_frequencia.Wrap( -1 )

		self.lb_frequencia.SetMinSize( wx.Size( 100,25 ) )

		lay_label_1.Add( self.lb_frequencia, 0, wx.ALL, 2 )


		lay_dispenser.Add( lay_label_1, 0, wx.EXPAND, 5 )

		lay_text_1 = wx.BoxSizer( wx.VERTICAL )

		lay_matricula = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_matricula = wx.TextCtrl( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.tc_matricula.SetMaxLength( 10 )
		lay_matricula.Add( self.tc_matricula, 0, wx.ALL, 2 )

		self.lb_situacao = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Situação:", wx.DefaultPosition, wx.Size( -1,25 ), wx.ALIGN_RIGHT )
		self.lb_situacao.Wrap( -1 )

		lay_matricula.Add( self.lb_situacao, 0, wx.ALL, 2 )

		cb_situacaoChoices = [ u"Ativo", u"Bloqueado", u"Cancelado" ]
		self.cb_situacao = wx.ComboBox( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,25 ), cb_situacaoChoices, 0 )
		lay_matricula.Add( self.cb_situacao, 0, wx.ALL, 2 )


		lay_text_1.Add( lay_matricula, 0, wx.EXPAND, 0 )

		self.tc_nome = wx.TextCtrl( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,25 ), 0 )
		self.tc_nome.SetMaxLength( 50 )
		lay_text_1.Add( self.tc_nome, 0, wx.ALL, 2 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_setor = wx.TextCtrl( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,25 ), 0 )
		self.tc_setor.SetMaxLength( 2 )
		bSizer14.Add( self.tc_setor, 0, wx.ALL, 2 )

		self.bt_fd_setor = wx.Button( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,25 ), 0 )

		self.bt_fd_setor.SetBitmap( wx.Bitmap( u"desingner/icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_fd_setor.SetBitmapDisabled( wx.Bitmap( u"desingner/icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		bSizer14.Add( self.bt_fd_setor, 0, wx.ALL, 2 )

		self.lb_nome_setor = wx.StaticText( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 330,25 ), 0|wx.BORDER_SIMPLE )
		self.lb_nome_setor.Wrap( -1 )

		self.lb_nome_setor.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer14.Add( self.lb_nome_setor, 0, wx.ALL, 2 )


		lay_text_1.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_funcao = wx.TextCtrl( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,25 ), 0 )
		bSizer15.Add( self.tc_funcao, 0, wx.ALL, 2 )

		self.bt_fd_funcao = wx.Button( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,25 ), 0 )

		self.bt_fd_funcao.SetBitmap( wx.Bitmap( u"desingner/icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_fd_funcao.SetBitmapDisabled( wx.Bitmap( u"desingner/icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		bSizer15.Add( self.bt_fd_funcao, 0, wx.ALL, 2 )

		self.lb_nome_funcao = wx.StaticText( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 330,25 ), 0|wx.BORDER_SIMPLE )
		self.lb_nome_funcao.Wrap( -1 )

		self.lb_nome_funcao.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer15.Add( self.lb_nome_funcao, 0, wx.ALL, 2 )


		lay_text_1.Add( bSizer15, 0, wx.EXPAND, 5 )

		lay_senha = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_senha = wx.TextCtrl( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.tc_senha.SetMaxLength( 10 )
		lay_senha.Add( self.tc_senha, 0, wx.ALL, 2 )

		self.cb_redefinir = wx.CheckBox( self.pn_data_fields, wx.ID_ANY, u"Redefinir com frequência", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		lay_senha.Add( self.cb_redefinir, 0, wx.ALL, 2 )


		lay_text_1.Add( lay_senha, 0, wx.EXPAND, 0 )

		lay_frequencia = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_frequencia = wx.TextCtrl( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,25 ), 0 )
		self.tc_frequencia.SetMaxLength( 3 )
		lay_frequencia.Add( self.tc_frequencia, 0, wx.ALL, 2 )

		self.m_staticText16 = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"dias", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_staticText16.Wrap( -1 )

		lay_frequencia.Add( self.m_staticText16, 0, wx.ALL, 2 )


		lay_frequencia.Add( ( 100, 25), 0, wx.EXPAND, 5 )

		self.lb_vigencia = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Expira em:", wx.DefaultPosition, wx.Size( 80,25 ), wx.ALIGN_RIGHT )
		self.lb_vigencia.Wrap( -1 )

		lay_frequencia.Add( self.lb_vigencia, 0, wx.ALL, 2 )

		self.tc_vigencia = wx.TextCtrl( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,25 ), wx.TE_READONLY )
		lay_frequencia.Add( self.tc_vigencia, 0, wx.ALL, 2 )


		lay_text_1.Add( lay_frequencia, 0, wx.EXPAND, 0 )


		lay_dispenser.Add( lay_text_1, 0, wx.EXPAND, 1 )


		self.pn_data_fields.SetSizer( lay_dispenser )
		self.pn_data_fields.Layout()
		lay_dispenser.Fit( self.pn_data_fields )
		self.sb_widgets.AddPage( self.pn_data_fields, u"Cadastro", False )
		self.pn_data_list = wx.Panel( self.sb_widgets, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
		lay_grid_list = wx.BoxSizer( wx.VERTICAL )

		self.mg_search = wx.grid.Grid( self.pn_data_list, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.mg_search.CreateGrid( 1, 2 )
		self.mg_search.EnableEditing( True )
		self.mg_search.EnableGridLines( True )
		self.mg_search.EnableDragGridSize( False )
		self.mg_search.SetMargins( 0, 0 )

		# Columns
		self.mg_search.SetColSize( 0, 100 )
		self.mg_search.SetColSize( 1, 400 )
		self.mg_search.EnableDragColMove( False )
		self.mg_search.EnableDragColSize( True )
		self.mg_search.SetColLabelSize( 30 )
		self.mg_search.SetColLabelValue( 0, u"Matrícula" )
		self.mg_search.SetColLabelValue( 1, u"Nome Usuário" )
		self.mg_search.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.mg_search.EnableDragRowSize( True )
		self.mg_search.SetRowLabelSize( 30 )
		self.mg_search.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.mg_search.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		lay_grid_list.Add( self.mg_search, 1, wx.EXPAND, 5 )


		self.pn_data_list.SetSizer( lay_grid_list )
		self.pn_data_list.Layout()
		lay_grid_list.Fit( self.pn_data_list )
		self.sb_widgets.AddPage( self.pn_data_list, u"Lista", False )

		lay_widgets.Add( self.sb_widgets, 1, wx.EXPAND |wx.ALL, 0 )


		lay_body.Add( lay_widgets, 1, wx.EXPAND, 5 )

		lay_botton = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.bt_search = wx.Button( self, wx.ID_ANY, u"Localizar", wx.DefaultPosition, wx.Size( 100,36 ), 0 )

		self.bt_search.SetBitmap( wx.Bitmap( u"desingner/icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_search.SetBitmapDisabled( wx.Bitmap( u"desingner/icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		bSizer7.Add( self.bt_search, 0, wx.ALL, 5 )

		self.bt_select = wx.Button( self, wx.ID_ANY, u"&Redefinir Senha", wx.DefaultPosition, wx.Size( -1,36 ), 0 )
		bSizer7.Add( self.bt_select, 0, wx.ALL, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 0 )


		lay_botton.Add( bSizer7, 1, wx.EXPAND, 5 )


		lay_body.Add( lay_botton, 0, wx.ALIGN_BOTTOM|wx.EXPAND, 0 )


		self.SetSizer( lay_body )
		self.Layout()

		# Connect Events
		self.bt_fd_setor.Bind( wx.EVT_BUTTON, self.ac_find_setor )
		self.bt_fd_funcao.Bind( wx.EVT_BUTTON, self.ac_find_funcao )
		self.tc_frequencia.Bind( wx.EVT_KILL_FOCUS, self.on_kill_focus )
		self.mg_search.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_grid_dclick )
		self.bt_search.Bind( wx.EVT_BUTTON, self.ac_search )
		self.bt_select.Bind( wx.EVT_BUTTON, self.on_reset_pass )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ac_find_setor( self, event ):
		event.Skip()

	def ac_find_funcao( self, event ):
		event.Skip()

	def on_kill_focus( self, event ):
		event.Skip()

	def on_grid_dclick( self, event ):
		event.Skip()

	def ac_search( self, event ):
		event.Skip()

	def on_reset_pass( self, event ):
		event.Skip()


