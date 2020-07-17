# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:04:54 2020

@author: manjg
"""
import datetime

def sized_text(txt):           
    spaces = 25 - len(txt)
    return txt + (" " * spaces)

def flip_date(dater):
    year = dater.year
    month = dater.month
    day = dater.day
    flipped = "{}/{}/{}".format(month, day, year)
    return flipped    