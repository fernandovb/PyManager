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
## Class TPFPES
###########################################################################

class TPFPES ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Consulta Pessoas", pos = wx.DefaultPosition, size = wx.Size( 480,400 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		lay_body = wx.BoxSizer( wx.VERTICAL )

		self.pn_body = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_campos = wx.BoxSizer( wx.VERTICAL )

		lay_pesquisa = wx.BoxSizer( wx.VERTICAL )

		self.pn_lista = wx.Panel( self.pn_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_lista = wx.BoxSizer( wx.VERTICAL )

		self.gd_resultado = wx.grid.Grid( self.pn_lista, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gd_resultado.CreateGrid( 0, 3 )
		self.gd_resultado.EnableEditing( True )
		self.gd_resultado.EnableGridLines( True )
		self.gd_resultado.EnableDragGridSize( False )
		self.gd_resultado.SetMargins( 0, 0 )

		# Columns
		self.gd_resultado.SetColSize( 0, 90 )
		self.gd_resultado.SetColSize( 1, 310 )
		self.gd_resultado.SetColSize( 2, 150 )
		self.gd_resultado.EnableDragColMove( False )
		self.gd_resultado.EnableDragColSize( True )
		self.gd_resultado.SetColLabelSize( 30 )
		self.gd_resultado.SetColLabelValue( 0, u"CÓDIGO" )
		self.gd_resultado.SetColLabelValue( 1, u"NOME" )
		self.gd_resultado.SetColLabelValue( 2, u"FEDERAL" )
		self.gd_resultado.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gd_resultado.EnableDragRowSize( True )
		self.gd_resultado.SetRowLabelSize( 30 )
		self.gd_resultado.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gd_resultado.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		lay_lista.Add( self.gd_resultado, 1, wx.EXPAND, 1 )


		self.pn_lista.SetSizer( lay_lista )
		self.pn_lista.Layout()
		lay_lista.Fit( self.pn_lista )
		lay_pesquisa.Add( self.pn_lista, 1, wx.EXPAND |wx.ALL, 1 )

		self.pn_dados = wx.Panel( self.pn_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pn_dados.Hide()

		lay_geral = wx.BoxSizer( wx.HORIZONTAL )

		lay_titulos = wx.BoxSizer( wx.VERTICAL )

		self.lb_codigo = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_codigo.Wrap( -1 )

		lay_titulos.Add( self.lb_codigo, 0, wx.ALL, 1 )

		self.lb_nome_formal = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Nome formal:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_nome_formal.Wrap( -1 )

		lay_titulos.Add( self.lb_nome_formal, 0, wx.ALL, 1 )

		self.lb_nome_alternativo = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Nome alternativo:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_nome_alternativo.Wrap( -1 )

		lay_titulos.Add( self.lb_nome_alternativo, 0, wx.ALL, 1 )

		self.lb_federal = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Cadastro Federal:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_federal.Wrap( -1 )

		lay_titulos.Add( self.lb_federal, 0, wx.ALL, 1 )


		lay_geral.Add( lay_titulos, 0, wx.EXPAND, 1 )

		lay_dados = wx.BoxSizer( wx.VERTICAL )

		self.tc_codigo = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_codigo.SetMaxLength( 6 )
		lay_dados.Add( self.tc_codigo, 0, wx.ALL, 1 )

		self.tc_nome_formal = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,26 ), 0 )
		lay_dados.Add( self.tc_nome_formal, 0, wx.ALL, 1 )

		self.tc_nome_alternativo = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,26 ), 0 )
		lay_dados.Add( self.tc_nome_alternativo, 0, wx.ALL, 1 )

		self.tc_federal = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,26 ), 0 )
		lay_dados.Add( self.tc_federal, 0, wx.ALL, 1 )


		lay_geral.Add( lay_dados, 1, wx.EXPAND, 1 )


		self.pn_dados.SetSizer( lay_geral )
		self.pn_dados.Layout()
		lay_geral.Fit( self.pn_dados )
		lay_pesquisa.Add( self.pn_dados, 1, wx.EXPAND |wx.ALL, 1 )


		lay_campos.Add( lay_pesquisa, 1, wx.EXPAND, 1 )

		lay_botoes = wx.BoxSizer( wx.VERTICAL )

		self.pn_botoes = wx.Panel( self.pn_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 1, 3, 0, 0 )

		self.bt_confirmar = wx.Button( self.pn_botoes, wx.ID_OK, u"Confirmar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bt_confirmar.Enable( False )

		gSizer1.Add( self.bt_confirmar, 0, wx.ALL|wx.EXPAND, 5 )

		self.bt_localizar = wx.Button( self.pn_botoes, wx.ID_FIND, u"Localizar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.bt_localizar, 0, wx.ALL|wx.EXPAND, 5 )

		self.bt_cancelar = wx.Button( self.pn_botoes, wx.ID_CANCEL, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.bt_cancelar, 0, wx.ALL|wx.EXPAND, 5 )


		self.pn_botoes.SetSizer( gSizer1 )
		self.pn_botoes.Layout()
		gSizer1.Fit( self.pn_botoes )
		lay_botoes.Add( self.pn_botoes, 0, wx.EXPAND, 1 )


		lay_campos.Add( lay_botoes, 0, wx.EXPAND, 1 )


		self.pn_body.SetSizer( lay_campos )
		self.pn_body.Layout()
		lay_campos.Fit( self.pn_body )
		lay_body.Add( self.pn_body, 1, wx.EXPAND |wx.ALL, 1 )


		self.SetSizer( lay_body )
		self.Layout()

		# Connect Events
		self.gd_resultado.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.ac_selecionar )
		self.bt_localizar.Bind( wx.EVT_BUTTON, self.ac_localizar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ac_selecionar( self, event ):
		event.Skip()

	def ac_localizar( self, event ):
		event.Skip()


