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
## Class TSLFNC
###########################################################################

class TSLFNC ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Consulta função", pos = wx.DefaultPosition, size = wx.Size( 480,400 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		lay_body = wx.BoxSizer( wx.VERTICAL )

		self.pn_body = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		lay_pesquisa = wx.BoxSizer( wx.VERTICAL )

		self.pn_lista = wx.Panel( self.pn_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_lista = wx.BoxSizer( wx.VERTICAL )

		self.gd_resultado = wx.grid.Grid( self.pn_lista, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gd_resultado.CreateGrid( 0, 2 )
		self.gd_resultado.EnableEditing( False )
		self.gd_resultado.EnableGridLines( False )
		self.gd_resultado.EnableDragGridSize( False )
		self.gd_resultado.SetMargins( 0, 0 )

		# Columns
		self.gd_resultado.SetColSize( 0, 90 )
		self.gd_resultado.SetColSize( 1, 310 )
		self.gd_resultado.EnableDragColMove( False )
		self.gd_resultado.EnableDragColSize( True )
		self.gd_resultado.SetColLabelSize( 30 )
		self.gd_resultado.SetColLabelValue( 0, u"CÓDIGO" )
		self.gd_resultado.SetColLabelValue( 1, u"DESCRIÇÃO" )
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

		lay_dados = wx.BoxSizer( wx.HORIZONTAL )

		lay_titulos = wx.BoxSizer( wx.VERTICAL )

		self.lb_codigo = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_codigo.Wrap( -1 )

		lay_titulos.Add( self.lb_codigo, 0, wx.ALL, 1 )

		self.lb_descricao = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_descricao.Wrap( -1 )

		lay_titulos.Add( self.lb_descricao, 0, wx.ALL, 1 )


		lay_dados.Add( lay_titulos, 0, wx.EXPAND, 1 )

		lay_campos = wx.BoxSizer( wx.VERTICAL )

		self.tc_codigo = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_codigo.SetMaxLength( 6 )
		lay_campos.Add( self.tc_codigo, 0, wx.ALL, 1 )

		self.tc_descricao = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,26 ), 0 )
		lay_campos.Add( self.tc_descricao, 0, wx.ALL, 1 )


		lay_dados.Add( lay_campos, 1, wx.EXPAND, 5 )


		self.pn_dados.SetSizer( lay_dados )
		self.pn_dados.Layout()
		lay_dados.Fit( self.pn_dados )
		lay_pesquisa.Add( self.pn_dados, 1, wx.EXPAND |wx.ALL, 1 )


		bSizer2.Add( lay_pesquisa, 1, wx.EXPAND, 5 )

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


		bSizer2.Add( lay_botoes, 0, wx.EXPAND, 5 )


		self.pn_body.SetSizer( bSizer2 )
		self.pn_body.Layout()
		bSizer2.Fit( self.pn_body )
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


