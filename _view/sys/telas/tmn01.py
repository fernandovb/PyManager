# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

wx.ID_EXECUTE = 1000

###########################################################################
## Class TMN01
###########################################################################

class TMN01 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu Principal", pos = wx.DefaultPosition, size = wx.Size( 883,620 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.mn_mn01 = wx.MenuBar( 0 )
		self.mn_sistema = wx.Menu()
		self.mi_config = wx.MenuItem( self.mn_sistema, wx.ID_ANY, u"Configuração", u"Abre painel de teste", wx.ITEM_NORMAL )
		self.mn_sistema.Append( self.mi_config )

		self.mi_exit = wx.MenuItem( self.mn_sistema, wx.ID_ANY, u"Sair", u"Encerra o sistema", wx.ITEM_NORMAL )
		self.mi_exit.SetBitmap( wx.Bitmap( u"desingner/icons/ac_sair_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.mn_sistema.Append( self.mi_exit )

		self.mn_mn01.Append( self.mn_sistema, u"Sistema" )

		self.SetMenuBar( self.mn_mn01 )

		self.tb_mn01 = self.CreateToolBar( wx.TB_FLAT, wx.ID_ANY )
		self.tb_mn01.SetToolBitmapSize( wx.Size( 26,26 ) )
		self.lb_executar = wx.StaticText( self.tb_mn01, wx.ID_ANY, u"Executar: ", wx.DefaultPosition, wx.Size( 68,-1 ), wx.ALIGN_RIGHT )
		self.lb_executar.Wrap( -1 )

		self.tb_mn01.AddControl( self.lb_executar )
		self.tc_executar = wx.TextCtrl( self.tb_mn01, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.tb_mn01.AddControl( self.tc_executar )
		self.mt_run = self.tb_mn01.AddLabelTool( wx.ID_EXECUTE, u"Executar", wx.Bitmap( u"desingner/icons/ac_executar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Executa comando.", None )

		self.tb_mn01.AddSeparator()

		self.mt_ok = self.tb_mn01.AddLabelTool( wx.ID_SAVE, u"OK", wx.Bitmap( u"desingner/icons/ac_confirmar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Confirma operação da tela", None )

		self.mt_cancel = self.tb_mn01.AddLabelTool( wx.ID_CANCEL, u"Fechar", wx.Bitmap( u"desingner/icons/ac_cancelar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Cancela operação da tela.", None )

		self.mt_find = self.tb_mn01.AddLabelTool( wx.ID_FIND, u"Localizar", wx.Bitmap( u"desingner/icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Localiza registro.", None )

		self.tb_mn01.AddSeparator()

		self.mt_insert = self.tb_mn01.AddLabelTool( wx.ID_ADD, u"Novo registro", wx.Bitmap( u"desingner/icons/ac_adicionar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Cria novo registro", None )

		self.mt_edit = self.tb_mn01.AddLabelTool( wx.ID_EDIT, u"Altera registro", wx.Bitmap( u"desingner/icons/ac_editar_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Altera registro atual", None )

		self.mt_delete = self.tb_mn01.AddLabelTool( wx.ID_DELETE, u"Inativa registro", wx.Bitmap( u"desingner/icons/ac_lixeira_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Inativa o registro atual", None )

		self.tb_mn01.AddSeparator()

		self.mt_print = self.tb_mn01.AddLabelTool( wx.ID_PRINT, u"Envia tela para impressora", wx.Bitmap( u"desingner/icons/ac_imprimir_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Envia dados da tela para impressora", None )

		self.mt_pdf = self.tb_mn01.AddLabelTool( wx.ID_PRINT, u"Envia tela para impressora", wx.Bitmap( u"desingner/icons/ac_pdf_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Gera arquivo PDF com dados da tela", None )

		self.tb_mn01.AddSeparator()

		self.mt_exit = self.tb_mn01.AddLabelTool( wx.ID_EXIT, u"Sair", wx.Bitmap( u"desingner/icons/ac_sair_16x16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Encerra seção em andamento.", None )

		self.tb_mn01.Realize()

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.sb_transaction = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer1.Add( self.sb_transaction, 1, wx.EXPAND |wx.ALL, 1 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.mn_timer = wx.Timer()
		self.mn_timer.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_exit )
		self.Bind( wx.EVT_MENU, self.ac_config, id = self.mi_config.GetId() )
		self.Bind( wx.EVT_MENU, self.on_exit, id = self.mi_exit.GetId() )
		self.tc_executar.Bind( wx.EVT_KEY_DOWN, self.on_keydown )
		self.Bind( wx.EVT_TOOL, self.ac_run, id = self.mt_run.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_ok, id = self.mt_ok.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_cancel, id = self.mt_cancel.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_find, id = self.mt_find.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_insert, id = self.mt_insert.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_edit, id = self.mt_edit.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_delete, id = self.mt_delete.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_print, id = self.mt_print.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_pdf, id = self.mt_pdf.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_exit, id = self.mt_exit.GetId() )
		self.Bind( wx.EVT_TIMER, self.on_timer, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_exit( self, event ):
		event.Skip()

	def ac_config( self, event ):
		event.Skip()


	def on_keydown( self, event ):
		event.Skip()

	def ac_run( self, event ):
		event.Skip()

	def on_ok( self, event ):
		event.Skip()

	def on_cancel( self, event ):
		event.Skip()

	def on_find( self, event ):
		event.Skip()

	def on_insert( self, event ):
		event.Skip()

	def on_edit( self, event ):
		event.Skip()

	def on_delete( self, event ):
		event.Skip()

	def on_print( self, event ):
		event.Skip()

	def on_pdf( self, event ):
		event.Skip()


	def on_timer( self, event ):
		event.Skip()


