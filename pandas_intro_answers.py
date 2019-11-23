#!/usr/bin/env python
# coding: utf-8

# This is a simple Python notebook demonstrating the power of pandas

# In[1]:


import pandas as pd

df = pd.read_csv('2018_General_Election_Returns.csv')

len_df = len(df)

print(f'Imported {len_df} rows')


# In[2]:


#printing all offices
offices = list(df['Office'].drop_duplicates())
num_offices = len(offices)
print(f'Found {num_offices} offices')


# In[3]:


#Finding results for first office
first_office = offices[0]

office_df = df[df['Office'] == first_office]

#Printing who ran in that office
candidates = ', '.join(list(office_df['Name'].drop_duplicates()))
print(f'Total votes: {candidates}')

#Printing total votes
total_votes = office_df['Votes'].sum()
print(f'Total votes: {total_votes}')


# In[ ]:


#Print list of all of the offices
print(', '.join(offices))

#Pick an office and list the candidates running for that office
my_office_df = df[df['Office'] == 'U.S. Rep 32']
print(', '.join(list(my_office_df['Name'].drop_duplicates())))

