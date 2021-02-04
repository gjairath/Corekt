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

def display_slots(time_array, mode):
    
    hs = []
    
    for item in time_array:
        if (item[0].find(mode) != -1):
            hs.append(item)
    
    print(hs)

def get_hour_vals(hour):
    hs = str()
    if (hour[1] == ":"):
        # singular hour
        hs = hour[0]
    else:
        hs = hour[0:2]
        
    return hs

def append_colon_zero(time_array):

    # Fix 11 or 12, it currently works for 6 - 7 type formats.
    # Then check again for now.
    
    # str.split() -> numeric value -> check if it has colon. 
    # fix whatever is the issue and combine it.
    # Permutations are stupid af.
    
    # '5 - 6 PM', '89 spots available'
    
    for idx, item in enumerate(time_array):
        hour_array = item[0].split()
        for idx_l, sub_str in enumerate(hour_array):
            if (sub_str.isnumeric()):
                if (sub_str.find(":") == -1):
                    hour_array[idx_l] = sub_str[:] + ":00"
                    
            time_array[idx][0] = " ".join(hour_array)
    
    return time_array
    
def print_deltas(idx, time_array):
    ta = append_colon_zero(time_array)
    
    print ("\n\n")
    
    print(ta[idx - 2][0] + "\t\t" + ta[idx - 2][1])
    print(ta[idx - 1][0] + "\t\t" +  ta[idx - 1][1])
    print(ta[idx][0] + "\t\t" + ta[idx][1])
    print(ta[idx + 1][0] + "\t\t" + ta[idx + 1][1])
    print(ta[idx + 2][0] + "\t\t" + ta[idx + 2][1])



def show_all_times(time_array):
    ta = append_colon_zero(time_array)

    for idx in range(len(ta)):
        print(ta[idx][0] + "\t\t{>8}".format( ta[idx][1] ))


def prettify(time_array):    
    
    
    print ("\t SHOWING SLOTS\n\n")    
        
    hour = input("FOR SPEED: For example 2:00 or 11:00.\nEnter: \t")
    mode_day = input("===============\n\nAM OR PM\nEnter:\t")
    user_pref = get_hour_vals(hour)
    
    # if the user says 11:45 take 11, traverse the time array and simply print a delta.
    idx = 0
    
    for loop_idx, item in enumerate(time_array):
        if (int(user_pref) >= 10):            
            if (item[0][0] == user_pref[0] and item[0][1] == user_pref[1] and item[0].find(mode_day) != -1):
                # This hour slot matches. 
                idx = loop_idx
        else:
            if (item[0][0] == user_pref[0] and item[0].find(mode_day) != -1):
                idx = loop_idx
    
    # show the deltas.
    print_deltas(idx, time_array)
    

    show_all = input("===============\n\nWould you like to see all options instead? :[Yes|No] \t")
    if (show_all == "Yes"): show_all_times(time_array)
    
        
    
    
        
prettify(test_array)