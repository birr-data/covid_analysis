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
from funcs import sized_text

#global vars
policies_list = []
policies = {}

program_run = True 


# ----------------------------------------remove after debug
pd.options.display.max_columns = None
pd.options.display.max_rows = None
#______________________________________________
#import data and clean up
covid_data = pd.read_csv('data/COVID Tracking - Historical.csv')
policy_data = pd.read_csv('data/Policy - Univ of Washington.csv') 

covid_data.drop('DATA_SOURCE_NAME',axis=1,inplace=True)
#covid_data.set_index('state',inplace=True)

policy_data.drop(['GLOBAL_BURDEN_DISEASE_IDENTIFIER',
                 'PROVINCE_STATE_FIPS_NUMBER', 'PROVINCE_STATE_NAME'],
                 axis=1, inplace=True)

# get distinct policies from table and create sorted dictionary for menu selection
policies_list = policy_data['POLICY_NAME'].unique()
policies_list.sort()
   
for i in range (0, len(policies_list)-1):
    #sized_text function for even column spacing        
    policies[i] = sized_text(policies_list[i])
    

        

def look():
    print(covid_data.head())
    print(covid_data.shape)
    print(policy_data.head())
    print(policy_data.shape)        
         
def interface():
    
    print("-----------    Covid-19 Policy analysis tool   ----------------") 
    print("- This utility facilitates analysis of government policy") 
    print("- effects on Covid-19 cases.\n")
    print("-  Select State: ")
    print("""
    - AK: Alaska           AL: Alabama         AR: Arkansas       AS: American Samoa
    - AZ: Arizona          CA: California      CO: Colorado       CT: Connecticut  
    - DC: Dist of Colum    DE: Delaware        FL: Florida        GA: Georgia             
    - GU: Guam             HI: Hawaii          IA: Iowa           ID: Idaho
    - IL: Illinois         IN: Indiana         KS: Kansas         KY: Kentucky
    - LA: Louisiana        MA: Massachusetts   MD: Maryland       ME: Maine 
    - MI: Michigan         MN: Minnesota       MO: Missouri       MP: Northern Mariana Is.
    - MS: Mississippi      MT: Montana         NA: National       NC: North Carolina
    - ND: North Dakota     NE: Nebraska        NH: New Hampshire  NJ: New Jersey
    - NM: New Mexico       NV: Nevada          NY: New York       OH: Ohio 
    - OK: Oklahoma         OR: Oregon          PA: Pennsylvania   PR: Puerto Rico
    - RI: Rhode Island     SC: South Carolina  SD: South Dakota   TN: Tennessee
    - TX: Texas            UT: Utah            VA: Virginia       VI: Virgin Islands 
    - VT: Vermont          WA: Washington      WI: Wisconsin      WV: West Virginia
    - WY: Wyoming""")
    
    valid_entry = False   
    while valid_entry == False:   
        state_selected = input("Enter State code (not case sensitive): ").upper()
        if (isinstance(state_selected, str) and (len(state_selected) == 2)):
            valid_entry = True
        else:
            print("Invalid entry, please try again.\n")
            
    print(state_selected)
      
    covid_state_data = covid_data.loc[covid_data['state'] == state_selected]
   
    covid_state_data.to_csv('filtered by state.csv')    
   
    print(covid_state_data.shape)
    
    
    
    row_count = int((len(policies)/3)) #diplay 3 columns
    for r in range(0, row_count + 1):
       print ("-  {}- {}  {}- {}  {}- {} ".format(r, policies.get(r), 
               r + row_count, policies.get(r + row_count), 
               r + (row_count * 2),policies.get(r + (row_count * 2)))) 
    valid_entry = False   
    while valid_entry == False:   
        sel = input("Enter a number or series of numbers separated by commas: ")
        for char in sel:
            if char.isdigit() == True:
                valid_entry = True
            elif char == " ":
                valid_entry = True
            elif char == ',':
                valid_entry = True
            else:
                valid_entry = False
                print("Invalid entry, please try again.\n")
                break
    print (sel)

               

while program_run:
    interface()
    ext = input("Press any key to run another analysis, or [q]uit: ")
    if ext.lower() == "q":
        program_run = False