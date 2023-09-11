#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the Excel file
file_path = 'school report of AP exams by state 2021-22.xls'
sheet_name = 'Total AP Schools'
df = pd.read_excel(file_path, sheet_name=sheet_name)


# In[2]:


# Print the first few rows to check the data
print(df.head())


# In[3]:


# Get the number of employees in each state in 2021
df_2021 = df[df['Year 2021'] == 2021]['State'].value_counts()

# Get the number of employees in each state in 2022
df_2022 = df[df['Year 2022'] == 2022]['State'].value_counts()

# Calculate the difference in the number of employees between 2021 and 2022
df_diff = df_2022 - df_2021

# Print the results
print(df_diff)


# In[4]:


# Load the Excel file with multiple worksheets
excel_file = pd.ExcelFile('school report of AP exams by state 2021-22.xls')


# In[5]:


# Create a dictionary to store dataframes with mulitple worksheets
dataframes = {}
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    dataframes[sheet_name] = df


# In[6]:


# Exclude the "NON-U.S./U.S.TERR/CAN" data from all dataframes
for sheet_name, df in dataframes.items():
    dataframes[sheet_name] = df[df['State'] != 'NON-U.S./U.S.TERR/CAN']


# In[7]:


import matplotlib.pyplot as plt

# Plot the data for each year using matplotlib
for year in ['Year 2021', 'Year 2022']:
    plt.figure(figsize=(12, 6))
    plt.title(f'Data for {year}')
    for sheet_name, df in dataframes.items():
        plt.plot(df['State'], df[year], label=sheet_name)

    plt.xlabel('State')
    plt.ylabel('Value')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()


# In[ ]:




