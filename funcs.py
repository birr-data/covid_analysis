# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:04:54 2020

@author: manjg
"""
def sized_text(txt):           
    spaces = 25 - len(txt)
    return txt + (" " * spaces)
    