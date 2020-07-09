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

#global vars
policies_list = []
policies = {}  

def look():
    print(covid_data.head())
    print(covid_data.shape)
    print(policy_data.head())
    print(policy_data.shape)
    


  
    
    
def data_load():
    #import data and clean up
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
   
    for i in range (1, len(policies_list)+1):
        policies[i] = policies_list[i-1]
        
    print(policies)
    
def interface():

    print("-----------    Covid-19 Policy analysis tool   ----------------") 
    print("- This utility facilitates analysis of government policy") 
    print("- effects on Covid-19 cases.\n")
    print("- Select Restriction(s): ")
    
    
    item_count = (len(policies))
    menu_row_count = int(item_count/3)
    menu_row_remainder = item_count%3
    print (menu_row_count)
    for r in range(1, menu_row_count + 1):
        #print (policies)
        print ("-  {}- {}  {}- {}  {}- {} \n".format(r, policies.get(r), 
                r + menu_row_count, policies.get(r + menu_row_count), 
                r + (menu_row_count * 2),policies.get(r + (menu_row_count * 2)))) 
        
    
    if menu_row_remainder == 1:
        print ("-                {}- {} \n".format(item_count, policies.get(item_count))) 
        
        
    elif menu_row_remainder == 2:
       print ("-   {}- {}         {}- {} \n".format(item_count - 1 , policies.get(tem_count  - 1),
                                                    tem_count  , policies.get(tem_count )))
        
                    
data_load()
interface()       