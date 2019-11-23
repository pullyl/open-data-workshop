#!/usr/bin/env python
# coding: utf-8

# This is a simple Python notebook demonstrating the power of numpy

# In[1]:


import pandas as pd
import numpy as np

df = pd.read_csv('2018_General_Election_Returns.csv')

len_df = len(df)

print(f'Imported {len_df} rows')


# In[2]:


def is_state_house(x):
    if 'State Rep' in x:
        return True

    return False

#Finding results for state house
df['is_state_house'] = df['Office'].apply(lambda x: is_state_house(x))
state_house_office_df = df[df['is_state_house'] == True]
print(len(state_house_office_df))

print(list(state_house_office_df))
rolled_sh = state_house_office_df.groupby('Office').sum().reset_index()[['Office', 'Votes']]
rolled_sh = rolled_sh.sort_values(by='Office')

#Perform some calculations on state house votes
print(len(rolled_sh))
print('Median is {med}'.format(med=np.median(rolled_sh['Votes'])))
print('Mean is {med}'.format(med=np.mean(rolled_sh['Votes'])))      
print('Max is {med}'.format(med=np.max(rolled_sh['Votes'])))      
print('Min is {med}'.format(med=np.min(rolled_sh['Votes'])))


# In[4]:





# In[5]:





# In[8]:


def is_state_senate(x):
    if 'State Sen' in x:
        return True

    return False

#Finding results for state house
df['is_state_sen'] = df['Office'].apply(lambda x: is_state_senate(x))
state_sen_office_df = df[df['is_state_sen'] == True]
print(len(state_sen_office_df))

print(list(state_sen_office_df))
rolled_ss = state_sen_office_df.groupby('Office').sum().reset_index()[['Office', 'Votes']]
rolled_ss = rolled_ss.sort_values(by='Office')

#Perform some calculations on state house votes
print(len(rolled_ss))
print('Median is {med}'.format(med=np.median(rolled_ss['Votes'])))
print('Mean is {med}'.format(med=np.mean(rolled_ss['Votes'])))      
print('Max is {med}'.format(med=np.max(rolled_ss['Votes'])))      
print('Min is {med}'.format(med=np.min(rolled_ss['Votes'])))


# In[ ]:




