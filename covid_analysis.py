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

def look():
    print(covid_data.head())
    print(covid_data.shape)
    print(policy_data.head())
    print(policy_data.shape)
def data_load():
    covid_data = pd.read_csv('data/COVID Tracking - Historical.csv')
    policy_data = pd.read_csv('data/Policy - Univ of Washington.csv')
    
    covid_data.drop('DATA_SOURCE_NAME',axis=1,inplace=True)
    covid_data.set_index('PROVINCE_STATE_CODE',inplace=True)
    
    policy_data.drop(['GLOBAL_BURDEN_DISEASE_IDENTIFIER',
                     'PROVINCE_STATE_FIPS_NUMBER', 'PROVINCE_STATE_NAME'],
                     axis=1, inplace=True)
    
    # get distinct policies from table and create dictionary for menu selection
    policies_list = policy_data['POLICY_NAME'].unique()
    policies_list.sort()
    policies = {}
    for i in range (1, len(policies_list)+1):
        policies[i] = policies_list[i-1]
    
    
   

def interface():
    print("-----------    Covid-19 Policy analysis tool   ----------------") 
    print("- This utility facilitates analysis of government policy") 
    print("- effects on Covid-19 cases.")


data_load()
interface()
# data import and clean up

