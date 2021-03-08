# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 00:59:26 2021

@author: garvi
"""


#test.py

date_full = "Mar 10 2021"
#I know that march 8 monday.
# I want to display WEDNESDAY

date_date = date_full.split(" ")[1]
deficit_days = int(date_date) - 8

current_day = "Monday"
day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

print(day_name[day_name.index(current_day) + deficit_days])