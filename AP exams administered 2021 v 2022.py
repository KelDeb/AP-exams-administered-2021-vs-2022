#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('school report of AP exams by state 2021-22.xls')


# In[2]:


data.head()


# In[3]:


data.describe()


# In[4]:


#Size of data
len(data)


# In[5]:


data.dtypes


# In[6]:


data.State.unique()


# In[7]:


data.size


# In[8]:


# Perform some basic analysis
# Calculate the total for each year
total_2021 = data['Year 2021'].sum()
total_2022 = data['Year 2022'].sum()


# In[9]:


# Calculate the average for each year
average_2021 = data['Year 2021'].mean()
average_2022 = data['Year 2022'].mean()


# In[10]:


# Calculate the maximum and minimum values for each year
max_2021 = data['Year 2021'].max()
min_2021 = data['Year 2021'].min()
max_2022 = data['Year 2022'].max()
min_2022 = data['Year 2022'].min()


# In[11]:


# Print the results
print(f"Total for 2021: {total_2021}")
print(f"Total for 2022: {total_2022}")
print(f"Average for 2021: {average_2021}")
print(f"Average for 2022: {average_2022}")
print(f"Maximum for 2021: {max_2021}")
print(f"Minimum for 2021: {min_2021}")
print(f"Maximum for 2022: {max_2022}")
print(f"Minimum for 2022: {min_2022}")


# In[12]:


# Calculate the change from Year 2021 to Year 2022
change = total_2022 - total_2021
print(f"Change from Year 2021 to Year 2022: {change}")


# In[13]:


# Calculate the state with the highest value for Year 2022
max_value_state_2022 = data[data['Year 2022'] == data['Year 2022'].max()]['State'].values[0]
print(f"State with the highest value in Year 2022: {max_value_state_2022}")


# In[14]:


# Calculate the state with the highest value for Year 2021
max_value_state_2021 = data[data['Year 2021'] == data['Year 2021'].max()]['State'].values[0]
print(f"State with the highest value in Year 2021: {max_value_state_2021}")


# In[15]:


# Calculate the state with the lowest value for Year 2021
min_value_state_2021 = data[data['Year 2021'] == data['Year 2021'].min()]['State'].values[0]
print(f"State with the lowest value in Year 2021: {min_value_state_2021}")


# In[16]:


# Calculate the state with the lowest value for Year 2022
min_value_state_2022 = data[data['Year 2022'] == data['Year 2022'].min()]['State'].values[0]
print(f"State with the lowest value in Year 2022: {min_value_state_2022}")


# In[17]:


import matplotlib.pyplot as plt
# Exclude 'NON-U.S./U.S.TERR/CAN' from the dataset
data = data[data['State'] != 'NON-U.S./U.S.TERR/CAN']


# In[18]:


# Calculate the average values for each year
avg_2021 = data['Year 2021'].mean()
avg_2022 = data['Year 2022'].mean()


# In[19]:


# Create a bar chart to visualize the data
plt.figure(figsize=(12, 6))
plt.bar(data['State'], data['Year 2021'], label='Year 2021')
plt.bar(data['State'], data['Year 2022'], label='Year 2022', alpha=0.9)
plt.xlabel('State')
plt.ylabel('Values')
plt.title('Year 2021 vs Year 2022 by State')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()


# In[20]:


# Show the average values
print(f'Average for Year 2021: {avg_2021:.2f}')
print(f'Average for Year 2022: {avg_2022:.2f}')


# In[21]:


# Save the plot to an image file
plt.savefig('data_analysis_plot.png')

# Show the plot
plt.show()


# In[22]:


# Calculate the change from Year 2021 to Year 2022
change = total_2022 - total_2021
print(f"Change from Year 2021 to Year 2022: {change}")


# In[23]:


# Calculate the state with the highest value for Year 2021
max_value_state_2021 = data[data['Year 2021'] == data['Year 2021'].max()]['State'].values[0]
print(f"State with the highest value in Year 2021: {max_value_state_2021}")


# In[24]:


# Calculate the state with the highest value for Year 2022
max_value_state_2022 = data[data['Year 2022'] == data['Year 2022'].max()]['State'].values[0]
print(f"State with the highest value in Year 2022: {max_value_state_2022}")


# In[ ]:




