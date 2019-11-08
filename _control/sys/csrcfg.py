# -*- coding: utf-8 -*-

import wx
from ObjectListView import ObjectListView

def getWidgets(parent):
    items = [parent]
    for item in parent.GetChildren():
        items.append(item)
        if hasattr(item, 'GetChildren'):
            for child in item.GetChildren():
                items.append(child)
    return items

def darkRowFormatter(listctrl, dark=False):
    listItems = [listctrl.GetItem(i) for i in range(listctrl.GetItemCount())]
    for index, item in enumerate(listItems):
        if dark:
            if index % 2:
                item.SetBackgroundColour('Dark Grey')
            else:
                item.SetBackgroundColour('Light Grey')
        else:
            if index % 2:
                item.SetBackgroundColour('Light Blue')
            else:
                item.SetBackgroundColour('Yellow')
        listctrl.SetItem(item)

def darkMode(self, normalPanelColor):
    widgets = getWidgets(self)
    panel = widgets[0]
    if normalPanelColor == panel.GetBackgroundColour():
       dark_mode = True
    else:
        dark_mode = False
    for widget in widgets:
        if dark_mode:
            if isinstance(widget, ObjectListView) or isinstance(widget, wx.ListCtrl):
                darkRowFormatter(widget, dark=True)
            widget.SetBackgroundColour('Dark Grey')
            widget.SetForegroundColour('White')
        else:
            if isinstance(widget, ObjectListView) or isinstance(widget, wx.ListCtrl):
                darkRowFormatter(widget)
                widget.SetBackgroundColour('White')
                widget.SetForegroundColour('Black')
                continue
            widget.SetBackgroundColour(wx.NullColour)
            widget.SetForegroundColour('Black')
    self.Refresh()
    return dark_mode