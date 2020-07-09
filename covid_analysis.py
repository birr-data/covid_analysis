# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:40:42 2020

@author: manjgom  
         birr.data@gmail.com
         
         Work modified and expanded from Coursera 
         Covid19 Data Analysis using Python course
         by Ahmad Varasteh
         
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

covid_data = pd.read_csv('data/COVID Tracking - Historical.csv')
policy_data = pd.read_csv('data/Policy - Univ of Washington.csv')

covid_data.drop('DATA_SOURCE_NAME',axis=1,inplace=True)
covid_data.set_index('PROVINCE_STATE_CODE',inplace=True)

print(covid_data.head())
print(covid_data.shape)