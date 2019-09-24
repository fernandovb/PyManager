# -*- coding: utf-8 -*-

from wx.lib.pubsub import pub
from _view.sys.telas.tsrcfg import TSRCFG



class SRCFG(TSRCFG):

    def __init__(self, parent):
        super(SRCFG, self).__init__(parent)

    def on_ok(self):
        pass

    def on_cancel(self):
        pass

    def on_close(self):
        pub.sendMessage('framePanel', message='close')
        self.Destroy()

    def on_apply(self, event):
        try:
            self.pn_data_fields.SetBackgroundColour(self.cp_background.GetColour())
            self.bt_apply.SetBackgroundColour(self.cp_button.GetColour())
            self.pn_data_fields.Refresh()
        except:
            self.tc_color_name.Value = 'Deu erro'
    
    def on_cp_background_killfocus(self, event):
        self.tc_color_name.Value = self.cp_background.GetName()
        