# -*- coding: utf-8 -*-

import wx
from wx.lib.pubsub import pub
from _view.sys.telas.tsrcfg import TSRCFG
from _control.sys.csrcfg import darkMode
from ObjectListView import ObjectListView


class SRCFG(TSRCFG):

    def __init__(self, parent):
        super(SRCFG, self).__init__(parent)
        self.defaultColour = self.GetBackgroundColour()
        darkMode(self.sb_widgets, self.defaultColour)
        darkMode(self, self.defaultColour)

    def on_ok(self):
        pass

    def on_cancel(self):
        pass
    
    def on_select(self, event):
        if self.cb_mode_theme.Value == 'Dark':
            self.cp_background.SetColour('Dark Grey')
            self.cp_foreground.SetColour('White')
        elif self.cb_mode_theme.Value == 'Light':
            self.cp_background.SetColour('White')
            self.cp_foreground.SetColour('Black')
        elif self.cb_mode_theme.Value == 'Night Theme':
            self.cp_background.SetColour('rgb(0, 0, 120)')
            self.cp_foreground.SetColour('Light Blue')
        elif self.cb_mode_theme.Value == 'Shades of Gray':
            self.cp_background.SetColour('rgb(64, 64, 64)')
            self.cp_foreground.SetColour('rgb(208, 208, 208)')
        self.tc_color_background.Value = wx.Colour(self.cp_background.GetColour()).GetAsString()
        self.tc_color_foreground.Value = wx.Colour(self.cp_foreground.GetColour()).GetAsString()

    def on_colour_background(self, event):
        self.tc_color_background.Value = wx.Colour(self.cp_background.GetColour()).GetAsString()

    def on_colour_foreground(self, event):
        self.tc_color_foreground.Value = wx.Colour(self.cp_foreground.GetColour()).GetAsString()

    def on_close(self):
        pub.sendMessage('framePanel', message='close')
        self.Destroy()

    def on_apply(self, event):
        self.app_theme(self.sb_widgets)
        self.app_theme(self)

    def app_theme(self, parent):
        try:
            widgets = self.getWidgets(parent)
            for widget in widgets:
                if isinstance(widget, ObjectListView) or isinstance(widget, wx.ListCtrl):
                    darkRowFormatter(widget, dark=True)
                widget.SetBackgroundColour(self.cp_background.GetColour())
                widget.SetForegroundColour(self.cp_foreground.GetColour())
        except:
            self.tc_color_name.Value = 'Deu erro'
        self.Refresh()

    def getWidgets(self, parent):
        items = [parent]
        for item in parent.GetChildren():
            items.append(item)
            if hasattr(item, 'GetChildren'):
                for child in item.GetChildren():
                    items.append(child)
        return items

    def on_cp_background_killfocus(self, event):
        self.tc_color_name.Value = self.cp_background.GetName()
