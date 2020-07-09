# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:40:42 2020

@author: manjgom  
         birr.data@gmail.com
             
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from dictionaries import states


print(states)

def look():
    print(covid_data.head())
    print(covid_data.shape)
    print(policy_data.head())
    print(policy_data.shape)
    

# data import and clean up
covid_data = pd.read_csv('data/COVID Tracking - Historical.csv')
policy_data = pd.read_csv('data/Policy - Univ of Washington.csv')

covid_data.drop('DATA_SOURCE_NAME',axis=1,inplace=True)
covid_data.set_index('PROVINCE_STATE_CODE',inplace=True)

policy_data.drop(['GLOBAL_BURDEN_DISEASE_IDENTIFIER',
                 'PROVINCE_STATE_FIPS_NUMBER', 'PROVINCE_STATE_NAME'],
                 axis=1, inplace=True)

look()