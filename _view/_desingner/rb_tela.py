# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.lib.agw.ribbon as rb

###########################################################################
## Class rb_tela
###########################################################################

class rb_tela ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ribbon Tela", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		self.m_ribbonBar2 = rb.RibbonBar( self , wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_BAR_DEFAULT_STYLE )
		self.m_ribbonPage2 = rb.RibbonPage( self.m_ribbonBar2, wx.ID_ANY, u"MyRibbonPage" , wx.NullBitmap , 0 )
		self.m_ribbonPanel2 = rb.RibbonPanel( self.m_ribbonPage2, wx.ID_ANY, u"MyRibbonPanel" , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.m_ribbonButtonBar2 = rb.RibbonButtonBar( self.m_ribbonPanel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_ribbonButtonBar2.AddSimpleButton( wx.ID_ANY, u"MyRibbonButton", wx.Bitmap( u"icons/ac_adicionar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.m_ribbonButtonBar2.AddDropdownButton( wx.ID_ANY, u"MyRibbonDropdownButton", wx.Bitmap( u"icons/ac_imprimir_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.m_ribbonBar2.Realize()

		bSizer38.Add( self.m_ribbonBar2, 1, wx.EXPAND, 5 )


		bSizer37.Add( bSizer38, 0, wx.EXPAND, 1 )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer40.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.m_textCtrl21, 0, wx.ALL, 5 )


		bSizer39.Add( bSizer40, 0, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.m_button1, 0, wx.ALL, 5 )


		bSizer37.Add( bSizer39, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer37 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_rb_button, id = wx.ID_ANY )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED, self.ac_drop_button, id = wx.ID_ANY )
		self.m_button1.Bind( wx.EVT_BUTTON, self.ac_button )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ac_rb_button( self, event ):
		event.Skip()

	def ac_drop_button( self, event ):
		event.Skip()

	def ac_button( self, event ):
		event.Skip()


