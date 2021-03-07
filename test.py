# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 03:59:03 2021

@author: garvi
"""
#test.py

ta = [['6:00 AM - 7:00 AM', '46 spots available'], ['6:20 AM - 7:40 AM', '46 spots available'], ['6:40 AM - 8:00 AM', '63 spots available'], ['7:00 AM - 8:00 AM', '64 spots available'], ['7:20 AM - 8:40 AM', '68 spots available'], ['7:40 AM - 9:00 AM', '69 spots available'], ['8:00 AM - 9:00 AM', '79 spots available'], ['8:20 AM - 9:40 AM', '67 spots available'], ['8:40 AM - 10:00 AM', '73 spots available'], ['9:00 AM - 10:00 AM', '73 spots available'], ['9:20 AM - 10:40 AM', '77 spots available'], ['9:40 AM - 11:00 AM', '76 spots available'], ['10:00 AM - 11:00 AM', '84 spots available'], ['10:20 AM - 11:40 AM', '83 spots available'], ['10:40 AM - 12:00 PM', '83 spots available'], ['11:00 AM - 12:00 PM', '83 spots available'], ['11:20 AM - 12:40 PM', '87 spots available'], ['11:40 AM - 1:00 PM', '77 spots available'], ['12:00 PM - 1:00 PM', '84 spots available'], ['12:20 PM - 1:40 PM', '89 spots available'], ['12:40 PM - 2:00 PM', '85 spots available'], ['1:00 PM - 2:00 PM', '85 spots available'], ['1:20 PM - 2:40 PM', '84 spots available'], ['1:40 PM - 3:00 PM', '83 spots available'], ['2:00 PM - 3:00 PM', '89 spots available'], ['2:20 PM - 3:40 PM', '87 spots available'], ['2:40 PM - 4:00 PM', '81 spots available'], ['3:00 PM - 4:00 PM', '80 spots available'], ['3:20 PM - 4:40 PM', '73 spots available'], ['3:40 PM - 5:00 PM', '76 spots available'], ['4:00 PM - 5:00 PM', '79 spots available'], ['4:20 PM - 5:40 PM', '80 spots available'], ['4:40 PM - 6:00 PM', '77 spots available'], ['5:00 PM - 6:00 PM', '84 spots available'], ['5:20 PM - 6:40 PM', '75 spots available'], ['5:40 PM - 7:00 PM', '82 spots available'], ['6:00 PM - 7:00 PM', '84 spots available'], ['6:20 PM - 7:40 PM', '79 spots available'], ['6:40 PM - 8:00 PM', '83 spots available'], ['7:00 PM - 8:00 PM', '85 spots available'], ['7:20 PM - 8:40 PM', '83 spots available'], ['7:40 PM - 9:00 PM', '84 spots available'], ['8:00 PM - 9:00 PM', '77 spots available'], ['8:20 PM - 9:40 PM', '82 spots available'], ['8:40 PM - 10:00 PM', '81 spots available'], ['9:00 PM - 10:00 PM', '88 spots available']]

u = "b 5 p S"
ud = u.split(" ")
time_char = ud[1][0]

time = time_char + ":00"

b = ud[2]

#Default
mode = "AM"

if (b[0] == "p" or b[0] == "P"):
    mode = "PM"
else:
    mode = "AM"

for idx, item in enumerate(ta):
    if (item[0].find(mode) != -1 and item[0].find(time) != -1): 
        print(item[0], idx + 1)