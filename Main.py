# module main.py
# -*- coding: utf-8 -*-
import clr
clr.AddReference('RevitAPI')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from Forms import Window

uiapp = __revit__                          # noqa
app = __revit__.Application                # noqa
doc = __revit__.ActiveUIDocument.Document  # noqa

__window__.Close() # noqa

if __name__ == '__main__':
    f = Window()
    f.ShowDialog()