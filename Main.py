# module main.py
# -*- coding: utf-8 -*-

import os
import sys
sys.path += [
    os.path.dirname(os.path.realpath(__file__)),
]
from Forms import Window

__window__.Close() # noqa

if __name__ == '__main__':
    f = Window()
    f.ShowDialog()
    
