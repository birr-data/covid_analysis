# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:40:42 2020

@author: manjgom  
         birr.data@gmail.com
             
"""

import pandas as pd
import numpy as np

import seaborn as sns
import statistics as  stats
import matplotlib.pyplot as plt
from dictionaries import states
from funcs import sized_text
from datetime import datetime


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
    '''debug function to look at data'''
    print('covid number data')
    print(covid_data.head())
    print(covid_data.shape)
    print('policy data')
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
                 
    #filter df by state selected      
    covid_state_data = covid_data[covid_data['PROVINCE_STATE_CODE'] == state_selected]
    #sort by date
    with pd.option_context('mode.chained_assignment', None):   # turns off SeetingWithCopyWarnning
        covid_state_data['REPORT_DATE_TYPE'] = covid_state_data['REPORT_DATE'].apply(lambda x : datetime.strptime(x, "%m/%d/%Y"))

        #**********************************************************************************************************
        
        
        
        #******************************   Date sorting is broken
        
        
        
        #need to convert date values to date data type for proper sort
        covid_state_data.sort_values(by=['REPORT_DATE'], inplace=True)
        covid_state_data.to_csv('state sorted by date.csv')
    #define axis values
    report_dates = covid_state_data['REPORT_DATE'].tolist()
    first_date_avail = report_dates[0]
    last_date_avail = report_dates[-1]
    requested_day_min = ""
    requested_day_max = ""
    # interface for selection of date range for report   
    valid_entry = False
    while valid_entry == False:
        # inform user of available date range - optio 'all' is available to select all dates
        date_entry =  input('''Enter desired date period for analysis in format:  m/d/yyyy-m/d/yyyy
        current available date range is {} to {}. 
        Entear [all] for all data or custom date range: '''.format(first_date_avail, last_date_avail))
        
        if date_entry.upper() == 'ALL':
            requested_date_min = first_date_avail
            requested_date_max = last_date_avail
            valid_entry = True
        else:
            delimiter = date_entry.find('-') 
            if delimiter!= -1:
                # if either date is not found on date list then invalid entry
                requested_date_max = date_entry[delimiter+1:]
                requested_date_min = date_entry[0:delimiter]
                if ((requested_date_max not in report_dates) or (requested_date_min not in report_dates)):
                    print("Invalid date format or date range entered. Please try again.") 
                else:
                    valid_entry = True
            else:
                print("Invalid date format or date range entered. Please try again.")
        #debug
        print (requested_date_min + "min") 
        print (requested_date_max + "max")    
        print (date_entry)
    
    
    #**************************
    covid_state_data_dated = covid_state_data[np.logical_and(covid_state_data['REPORT_DATE'] >= requested_date_min, covid_state_data['REPORT_DATE'] <= requested_date_max)]
    covid_state_data_dated.to_csv('dated_file.csv')
    #print (covid_state_data.shape)
    #print (covid_state_data_dated.shape)    
    
    #print (first_date_avail)   --- debug
    #print (last_date_avail)    --- degbug
    y = covid_state_data_dated['PEOPLE_DEATH_NEW_COUNT'].tolist()
    print(y)
    print('Daily Death Count Descriptive Statistics:')
    print('All available dates: {}-{}'.format(first_date_avail, last_date_avail))
    print('Mean   {:.4}'.format(float(stats.mean(y))))
    print('Median {:.4}'.format(float(stats.median(y))))
    print('Max    {:.4}'.format(float(max(y))))
    print('Min    {:.4}'.format(float(min(y))))
    
    max_tick = int(covid_state_data.shape[0]/7)
    
    # figure plotting
    plt.scatter(report_dates,y,s=10)
   
    ''' Draw trend line  https://www.dummies.com/programming/create-advanced-scatterplots-matplotlib/ '''
    #z = np.polyfit(x, y, 1)
    #p = np.poly1d(z)
    #plt.plot(x, p(x), 'm-')
        
    plt.xlabel ("Date")
    plt.axes().xaxis.set_major_locator(plt.MaxNLocator(max_tick))
    plt.xticks(rotation=90, fontsize=5)
    plt.ylabel ("Count")
    plt.title ("Covid-19 Daily Death Count\n " + states[state_selected])
    plt.show()
    
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