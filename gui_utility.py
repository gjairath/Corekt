# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 00:36:34 2021

@author: garvi
"""

test_array = [['6 - 7 AM', '89 spots available'], ['6:20 - 7:40 AM', '89 spots available'], ['6:40 - 8 AM', '89 spots available'], ['7 - 8 AM', '90 spots available'], ['7:20 - 8:40 AM', '89 spots available'], ['7:40 - 9 AM', '90 spots available'], ['8 - 9 AM', '88 spots available'], ['8:20 - 9:40 AM', '84 spots available'], ['8:40 - 10 AM', '89 spots available'], ['9 - 10 AM', '90 spots available'], ['9:20 - 10:40 AM', '90 spots available'], ['9:40 - 11 AM', '88 spots available'], ['10 - 11 AM', '90 spots available'], ['10:20 - 11:40 AM', '90 spots available'], ['10:40 AM - 12 PM', '89 spots available'], ['11 AM - 12 PM', '90 spots available'], ['11:20 AM - 12:40 PM', '90 spots available'], ['11:40 AM - 1 PM', '88 spots available'], ['12 - 1 PM', '89 spots available'], ['12:20 - 1:40 PM', '90 spots available'], ['12:40 - 2 PM', '87 spots available'], ['1 - 2 PM', '88 spots available'], ['1:20 - 2:40 PM', '90 spots available'], ['1:40 - 3 PM', '87 spots available'], ['2 - 3 PM', '90 spots available'], ['2:20 - 3:40 PM', '89 spots available'], ['2:40 - 4 PM', '90 spots available'], ['3 - 4 PM', '90 spots available'], ['3:20 - 4:40 PM', '90 spots available'], ['3:40 - 5 PM', '88 spots available'], ['4 - 5 PM', '89 spots available'], ['4:20 - 5:40 PM', '90 spots available'], ['4:40 - 6 PM', '89 spots available'], ['5 - 6 PM', '89 spots available'], ['5:20 - 6:40 PM', '90 spots available'], ['5:40 - 7 PM', '88 spots available'], ['6 - 7 PM', '89 spots available'], ['6:20 - 7:40 PM', '90 spots available'], ['6:40 - 8 PM', '89 spots available'], ['7 - 8 PM', '90 spots available'], ['7:20 - 8:40 PM', '90 spots available'], ['7:40 - 9 PM', '89 spots available'], ['8 - 9 PM', '90 spots available'], ['8:20 - 9:40 PM', '90 spots available'], ['8:40 - 10 PM', '90 spots available'], ['9 - 10 PM', '90 spots available']]


def number_of_AMs(time_array):
    counter = 0
    for item in time_array:
        if (item[0].find("AM") != -1):
            counter += 1;

    return counter

def get_slots(time_array, mode):
    
    hs = []
    
    if (mode == 1): sub_str = "AM"
    else: sub_str = "PM" 
        
    for item in time_array:
        time_str = item[0]
        
        if (time_str.find(sub_str) != -1):    
            # This is very self explanatory, fuck explanations. Good luck to the nerd
            # who inherited this from me.
            
            if (time_str[1] == ":"): first_letter = time_str[0:1]
            else: first_letter = time_str[0:2]
                        
            hs.append(first_letter)
        
        else:
            continue
    
    return hs


def get_hour_vals(hour):
    hs = str()
    if (hour[1] == ":"):
        # singular hour
        hs = hour[0]
    else:
        hs = hour[0:2]
        
    return hs
    
    

def prettify(time_array):    
    
    print(time_array)
    
    print ("\t SHOWING SLOTS\n\n")    
        
    hour = input("FOR SPEED: simply enter a time of day, \nany general vicinity is fine. \nFor example 2:00 or 11:00 Do NOT other formats.\n\nEnter the value here:\t")
    mode_day = input("\n\nEnter mode of day.\n1 for AM \n2 for PM for speed\n\nEnter the value here:\t")
    
    hour_slots = get_slots(test_array, mode_day)
    user_preference = get_hour_vals(hour)
    
    print (hour_slots)
    print (user_preference)
    
    
    
    # if the user says 11:45 take 11, traverse the time arrayand simply print a delta.
    # YOu can print all the hour slots for lols too. 

    desired_idx = 0 # by default just show this.

    for idx, hours in enumerate(hour_slots):
        if (hours == user_preference):
            desired_idx = idx
    
    offset_idx = 0
    if (mode_day == 2):
        # Idiot entered PM
        offset_idx = number_of_AMs(time_array)
        
    print (time_array[offset_idx + desired_idx - 2])
    print (time_array[offset_idx + desired_idx - 1])
    print (time_array[offset_idx + desired_idx])
    print (time_array[offset_idx + desired_idx + 1])
    print (time_array[offset_idx + desired_idx + 2])
    
prettify(test_array)