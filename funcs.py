# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:04:54 2020

@author: manjg
"""
import os
import shutil
from time import sleep
import datetime
import pandas as pd

       

def sized_text(txt):
    '''Adds spaces to make string 25 characters wide for column spacing.'''
    spaces = 25 - len(txt)
    return txt + (" " * spaces)

def flip_date(dater):
    ''' Takes datetime object, returns date string in mm/dd/yyyy format.'''
    year = dater.year
    month = dater.month
    day = dater.day
    flipped = "{}/{}/{}".format(month, day, year)
    return flipped  

def get_data():
    '''Download Covid-19 tracking dataset'''
    
    selection = input("Enter [y] to update data, enter [any] other key to continue with current data :")
    if selection.upper() == 'Y':
        print("Updating databases.")
        #set path for archives, create if it does not exist
        root = os.path.abspath(os.curdir)
        path = root + '/data/archive/covid_case_data/'
        if not os.path.isdir(path):
            os.makedirs(path)
        
        #copy current data to archive folder and number sequentially
        backup_files = os.listdir(path)
        new_achive = "COVID Tracking - Historical " + str(len(backup_files) + 1) + ".csv"
        shutil.copyfile('data/COVID Tracking - Historical.csv', path + new_achive)
        #delete old file
        os.remove('data/COVID Tracking - Historical.csv')
        print("Updating databases...")
        #download new data
        df = pd.read_csv('https://query.data.world/s/4bdfayuvydhxq3sapgzzgtlwom5xf4')
        print("Updating databases.....")
        df.to_csv('data/COVID Tracking - Historical.csv')

    
    
    
    
    
    
    
    
    
    