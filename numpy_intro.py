#!/usr/bin/env python
# coding: utf-8

# This is a simple Python notebook demonstrating the power of numpy

# In[1]:


import pandas as pd
import numpy as np

df = pd.read_csv('2018_General_Election_Returns.csv')

len_df = len(df)

print(f'Imported {len_df} rows')


# In[9]:


def is_state_house(x):
    if 'State Rep' in x:
        return True

    return False

#Finding results for state house
df['is_state_house'] = df['Office'].apply(lambda x: is_state_house(x))
office_df = df[df['is_state_house'] == True]
print(len(office_df))


# In[22]:


print(list(office_df))
rolled = office_df.groupby('Office').sum().reset_index()[['Office', 'Votes']]
rolled = rolled.sort_values(by='Office')


# In[31]:


#Perform some calculations on state house votes
print(len(rolled))
print('Median is {med}'.format(med=np.median(rolled['Votes'])))
print('Mean is {med}'.format(med=np.mean(rolled['Votes'])))      
print('Max is {med}'.format(med=np.max(rolled['Votes'])))      
print('Min is {med}'.format(med=np.min(rolled['Votes'])))


# In[ ]:




