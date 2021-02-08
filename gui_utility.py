# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 00:36:34 2021

@author: garvi
"""

ta = [['6:00 AM - 7:00 AM', '46 spots available'], ['6:20 AM - 7:40 AM', '46 spots available'], ['6:40 AM - 8:00 AM', '63 spots available'], ['7:00 AM - 8:00 AM', '64 spots available'], ['7:20 AM - 8:40 AM', '68 spots available'], ['7:40 AM - 9:00 AM', '69 spots available'], ['8:00 AM - 9:00 AM', '79 spots available'], ['8:20 AM - 9:40 AM', '67 spots available'], ['8:40 AM - 10:00 AM', '73 spots available'], ['9:00 AM - 10:00 AM', '73 spots available'], ['9:20 AM - 10:40 AM', '77 spots available'], ['9:40 AM - 11:00 AM', '76 spots available'], ['10:00 AM - 11:00 AM', '84 spots available'], ['10:20 AM - 11:40 AM', '83 spots available'], ['10:40 AM - 12:00 PM', '83 spots available'], ['11:00 AM - 12:00 PM', '83 spots available'], ['11:20 AM - 12:40 PM', '87 spots available'], ['11:40 AM - 1:00 PM', '77 spots available'], ['12:00 PM - 1:00 PM', '84 spots available'], ['12:20 PM - 1:40 PM', '89 spots available'], ['12:40 PM - 2:00 PM', '85 spots available'], ['1:00 PM - 2:00 PM', '85 spots available'], ['1:20 PM - 2:40 PM', '84 spots available'], ['1:40 PM - 3:00 PM', '83 spots available'], ['2:00 PM - 3:00 PM', '89 spots available'], ['2:20 PM - 3:40 PM', '87 spots available'], ['2:40 PM - 4:00 PM', '81 spots available'], ['3:00 PM - 4:00 PM', '80 spots available'], ['3:20 PM - 4:40 PM', '73 spots available'], ['3:40 PM - 5:00 PM', '76 spots available'], ['4:00 PM - 5:00 PM', '79 spots available'], ['4:20 PM - 5:40 PM', '80 spots available'], ['4:40 PM - 6:00 PM', '77 spots available'], ['5:00 PM - 6:00 PM', '84 spots available'], ['5:20 PM - 6:40 PM', '75 spots available'], ['5:40 PM - 7:00 PM', '82 spots available'], ['6:00 PM - 7:00 PM', '84 spots available'], ['6:20 PM - 7:40 PM', '79 spots available'], ['6:40 PM - 8:00 PM', '83 spots available'], ['7:00 PM - 8:00 PM', '85 spots available'], ['7:20 PM - 8:40 PM', '83 spots available'], ['7:40 PM - 9:00 PM', '84 spots available'], ['8:00 PM - 9:00 PM', '77 spots available'], ['8:20 PM - 9:40 PM', '82 spots available'], ['8:40 PM - 10:00 PM', '81 spots available'], ['9:00 PM - 10:00 PM', '88 spots available']]

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
        
        new_arr = []
        if (item[0].split()[1] == "-" and item[0].split()[1] != item[0].split()[3]):
            new_arr.append(item[0].split()[0])  
            new_arr.append(item[0].split()[3]) 
            new_arr.extend(item[0].split()[1:])
        
        if(new_arr != []): time_array[idx][0] = " ".join(new_arr)

    
    return time_array
    
def print_deltas(idx, time_array):
    ta = append_colon_zero(time_array)
    
    print ("\n\n")
    if(idx > 2 and ta[idx - 2]): print("[" + str(idx - 2 + 1) + "] " + ta[idx - 2][0] + "\t\t" + ta[idx - 2][1])
    if(idx > 1 and ta[idx - 1]): print("[" + str(idx - 1 + 1) + "] " + ta[idx - 1][0] + "\t\t" +  ta[idx - 1][1])
    if(ta[idx]): print("[" + str(idx + 1) + "] " + ta[idx][0] + "\t\t" + ta[idx][1])
    
    if (idx < len(time_array) - 2):
        print("[" + str(idx + 1 + 1) + "] " + ta[idx + 1][0] + "\t\t" + ta[idx + 1][1])
        print("[" + str(idx + 2 + 1) + "] " + ta[idx + 2][0] + "\t\t" + ta[idx + 2][1])


    return ta

def prettify(time_array, day, choice):    
    
    
    print ("\t SHOWING SLOTS for: {}\n\n".format(day[int(choice) - 1]))    
        
    hour = input("Enter a time, for example 2:00 or 11:00.\nEnter: \t")
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
    time_array = print_deltas(idx, time_array)