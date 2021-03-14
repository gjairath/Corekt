# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 22:10:56 2021

@author: garvi
"""


from datetime import date
import calendar
my_date = date.today()
# 7 days in a week lol
total_days = (len(calendar.day_name))

today = calendar.day_name[my_date.weekday()]
tomorrow = calendar.day_name[(my_date.weekday() + 1) % total_days]
day_after = calendar.day_name[(my_date.weekday() + 2) % total_days]

print ("\n If days are empty, 1 - {}, 2 - {}, 3 - {}".format(today, tomorrow, day_after))
