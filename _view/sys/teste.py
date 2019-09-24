# -*- coding: utf-8 -*-

from wx.lib.pubsub import pub
from _view.sys.telas.tteste import TTESTE


class TESTE(TTESTE):
	
	def __init__(self, parent):
		super(TESTE, self).__init__(parent)
	
	def on_close(self, event):
		pub.sendMessage('framePanel', message='close')
		self.Destroy()
