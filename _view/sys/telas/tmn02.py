# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class TMN02
###########################################################################

class TMN02 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.BORDER_THEME|wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		lay_body = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		lay_modulos = wx.BoxSizer( wx.VERTICAL )

		self.m_listbook2 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		m_listbook2ImageSize = wx.Size( 64,64 )
		m_listbook2Index = 0
		m_listbook2Images = wx.ImageList( m_listbook2ImageSize.GetWidth(), m_listbook2ImageSize.GetHeight() )
		self.m_listbook2.AssignImageList( m_listbook2Images )

		lay_modulos.Add( self.m_listbook2, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( lay_modulos, 1, wx.EXPAND, 1 )

		lay_transacoes = wx.BoxSizer( wx.VERTICAL )


		bSizer5.Add( lay_transacoes, 0, wx.EXPAND, 1 )

		lay_inform = wx.BoxSizer( wx.VERTICAL )

		self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		lay_inform.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( lay_inform, 0, wx.EXPAND, 1 )


		lay_body.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( lay_body )
		self.Layout()

	def __del__( self ):
		pass


