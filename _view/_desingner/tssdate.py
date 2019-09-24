# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class TSSDATE
###########################################################################

class TSSDATE ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Selecionar Data", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		lay_body = wx.BoxSizer( wx.VERTICAL )

		lay_calendar = wx.BoxSizer( wx.VERTICAL )

		self.cl_calendario = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		lay_calendar.Add( self.cl_calendario, 0, wx.ALL, 1 )


		lay_body.Add( lay_calendar, 1, wx.EXPAND, 5 )

		lay_campos = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_data = wx.StaticText( self, wx.ID_ANY, u"Data:", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_RIGHT )
		self.lb_data.Wrap( -1 )

		lay_campos.Add( self.lb_data, 1, wx.ALL, 5 )

		self.dp_data = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 110,26 ), wx.adv.DP_DEFAULT )
		lay_campos.Add( self.dp_data, 0, wx.ALL, 5 )


		lay_body.Add( lay_campos, 0, wx.EXPAND, 5 )

		lay_botao = wx.GridSizer( 1, 2, 0, 0 )

		self.bt_confirmar = wx.Button( self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		lay_botao.Add( self.bt_confirmar, 0, wx.EXPAND, 5 )

		self.bt_cancelar = wx.Button( self, wx.ID_CANCEL, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		lay_botao.Add( self.bt_cancelar, 0, wx.EXPAND, 5 )


		lay_body.Add( lay_botao, 0, wx.BOTTOM|wx.EXPAND, 5 )


		self.SetSizer( lay_body )
		self.Layout()
		lay_body.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.cl_calendario.Bind( wx.adv.EVT_CALENDAR_DAY, self.ac_day )
		self.cl_calendario.Bind( wx.adv.EVT_CALENDAR_MONTH, self.ac_month )
		self.cl_calendario.Bind( wx.adv.EVT_CALENDAR_YEAR, self.ac_year )
		self.dp_data.Bind( wx.adv.EVT_DATE_CHANGED, self.ac_data_change )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ac_day( self, event ):
		event.Skip()

	def ac_month( self, event ):
		event.Skip()

	def ac_year( self, event ):
		event.Skip()

	def ac_data_change( self, event ):
		event.Skip()


