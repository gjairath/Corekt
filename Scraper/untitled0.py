# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:16:00 2021

@author: garvi
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

day = ['Tuesday', 'Monday', 'Monday', 'Monday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Friday', 'Friday', 'Friday', 'Friday', 'Friday', 'Tuesday', 'Tuesday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Friday', 'Friday', 'Friday', 'Friday', 'Friday', 'Friday', 'Thursday', 'Tuesday', 'Monday', 'Sunday', 'Saturday']



l = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

df = pd.DataFrame({'freq': day})

df.groupby('freq', as_index=True).size().sort_values().plot(kind='bar', orientation='vertical')

plt.xticks(rotation='horizontal')
plt.xlabel("The Days")
plt.ylabel("Frequency/Number of Days")
plt.title("Frequency of Days Showed")
plt.show()


explode=(0.12, 0.12, 0.12, 0.12, 0.12, 0.12)
df.value_counts().plot(kind='pie', labels = l, title = "Pie Chart for Days Booked", \
                      shadow = True, autopct='%1.1f%%', ylabel = "",explode = explode, pctdistance=0.65)
    
plt.show()
    