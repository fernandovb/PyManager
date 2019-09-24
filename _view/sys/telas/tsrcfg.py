# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class TSRCFG
###########################################################################

class TSRCFG ( wx.Panel ):

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

		self.lb_transaction_code1 = wx.StaticText( self.pn_title, wx.ID_ANY, u"SRCFG", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
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
		self.pn_data_fields.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		lay_dispenser = wx.BoxSizer( wx.HORIZONTAL )

		lay_label_1 = wx.BoxSizer( wx.VERTICAL )

		self.lb_fundo = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Cor do Fundo:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lb_fundo.Wrap( -1 )

		self.lb_fundo.SetMinSize( wx.Size( 100,25 ) )

		lay_label_1.Add( self.lb_fundo, 0, wx.ALL, 2 )

		self.lb_fundo1 = wx.StaticText( self.pn_data_fields, wx.ID_ANY, u"Cor do Botão:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lb_fundo1.Wrap( -1 )

		self.lb_fundo1.SetMinSize( wx.Size( 100,25 ) )

		lay_label_1.Add( self.lb_fundo1, 0, wx.ALL, 5 )


		lay_dispenser.Add( lay_label_1, 0, wx.EXPAND, 5 )

		lay_text_1 = wx.BoxSizer( wx.VERTICAL )

		lay_cor_fundo = wx.BoxSizer( wx.HORIZONTAL )

		self.cp_background = wx.ColourPickerCtrl( self.pn_data_fields, wx.ID_ANY, wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ), wx.DefaultPosition, wx.Size( 100,25 ), wx.CLRP_DEFAULT_STYLE )
		lay_cor_fundo.Add( self.cp_background, 0, wx.ALL, 2 )

		self.tc_color_name = wx.TextCtrl( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		lay_cor_fundo.Add( self.tc_color_name, 0, wx.ALL, 2 )


		lay_text_1.Add( lay_cor_fundo, 0, wx.EXPAND, 0 )

		lay_cor_botao = wx.BoxSizer( wx.HORIZONTAL )

		self.cp_button = wx.ColourPickerCtrl( self.pn_data_fields, wx.ID_ANY, wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ), wx.DefaultPosition, wx.Size( 100,25 ), wx.CLRP_DEFAULT_STYLE )
		lay_cor_botao.Add( self.cp_button, 0, wx.ALL, 2 )

		self.tc_color_name_button = wx.TextCtrl( self.pn_data_fields, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		lay_cor_botao.Add( self.tc_color_name_button, 0, wx.ALL, 2 )


		lay_text_1.Add( lay_cor_botao, 1, wx.EXPAND, 5 )


		lay_dispenser.Add( lay_text_1, 0, wx.EXPAND, 1 )


		self.pn_data_fields.SetSizer( lay_dispenser )
		self.pn_data_fields.Layout()
		lay_dispenser.Fit( self.pn_data_fields )
		self.sb_widgets.AddPage( self.pn_data_fields, u"Cadastro", False )

		lay_widgets.Add( self.sb_widgets, 1, wx.EXPAND |wx.ALL, 0 )


		lay_body.Add( lay_widgets, 1, wx.EXPAND, 5 )

		lay_botton = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.bt_apply = wx.Button( self, wx.ID_ANY, u"Aplicar", wx.DefaultPosition, wx.Size( -1,36 ), 0 )
		bSizer7.Add( self.bt_apply, 0, wx.ALL, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 0 )


		lay_botton.Add( bSizer7, 1, wx.EXPAND, 5 )


		lay_body.Add( lay_botton, 0, wx.ALIGN_BOTTOM|wx.EXPAND, 0 )


		self.SetSizer( lay_body )
		self.Layout()

		# Connect Events
		self.cp_background.Bind( wx.EVT_KILL_FOCUS, self.on_cp_background_killfocus )
		self.cp_button.Bind( wx.EVT_KILL_FOCUS, self.on_cp_background_killfocus )
		self.bt_apply.Bind( wx.EVT_BUTTON, self.on_apply )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_cp_background_killfocus( self, event ):
		event.Skip()


	def on_apply( self, event ):
		event.Skip()


