# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 00:10:27 2021

@author: garvi
"""


# automate_utility.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import gui_utility as gui

REPLACE_ME = [['Tuesday', 'Monday', 'Monday', 'Monday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Friday', 'Friday', 'Friday', 'Friday', 'Friday', 'Tuesday', 'Tuesday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Friday', 'Friday', 'Friday', 'Friday', 'Friday', 'Friday', 'Thursday', 'Tuesday', 'Monday', 'Sunday', 'Saturday'], ['Nov 24 2020', 'Nov 23 2020', 'Nov 23 2020', 'Nov 23 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 17 2020', 'Nov 17 2020', 'Aug 23 2020', 'Aug 23 2020', 'Aug 23 2020', 'Aug 23 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 12 2020', 'Nov 10 2020', 'Nov 9 2020', 'Nov 8 2020', 'Nov 7 2020'], '\nGarvit', ['5:00 PM to 6:00 PM ', '7:40 PM to 9:00 PM ', '7:20 PM to 8:40 PM ', '7:00 PM to 8:00 PM ', '5:40 PM to 7:00 PM ', '5:20 PM to 6:40 PM ', '5:00 PM to 6:00 PM ', '4:40 PM to 6:00 PM ', '4:20 PM to 5:40 PM ', '4:00 PM to 5:00 PM ', '4:40 PM to 6:00 PM ', '4:20 PM to 5:40 PM ', '4:00 PM to 5:00 PM ', '3:40 PM to 5:00 PM ', '2:40 PM to 4:00 PM ', '12:40 PM to 2:00 PM ', '12:00 PM to 1:00 PM ', '5:00 PM to 6:00 PM ', '4:40 PM to 6:00 PM ', '4:20 PM to 5:40 PM ', '3:40 PM to 5:00 PM ', '3:00 PM to 4:00 PM ', '3:00 PM to 4:00 PM ', '2:40 PM to 4:00 PM ', '4:00 PM to 5:00 PM ', '3:40 PM to 5:00 PM ', '2:40 PM to 4:00 PM ', '1:40 PM to 3:00 PM ', '4:40 PM to 6:00 PM ', '4:20 PM to 5:40 PM ', '4:00 PM to 5:00 PM ', '3:40 PM to 5:00 PM ', '3:00 PM to 4:00 PM ', '2:00 PM to 3:00 PM ', '1:00 PM to 2:00 PM ', '11:40 AM to 1:00 PM ', '9:00 AM to 10:00 AM ', '6:00 PM to 7:00 PM ', '10:00 AM to 11:00 AM ', '8:20 AM to 9:40 AM ', '7:20 AM to 8:40 AM ', '1:20 PM to 2:40 PM ', '10:20 AM to 11:40 AM ', '1:20 PM to 2:40 PM ', '7:40 AM to 9:00 AM ', '9:20 AM to 10:40 AM ', '11:00 AM to 12:00 PM ', '9:00 AM to 10:00 AM '], ['Tuesday Tue, Nov 24 2020 5:00 PM to 6:00 PM n/a Tue, Nov 24 2020 3:16 PM', 'Monday Mon, Nov 23 2020 7:40 PM to 9:00 PM n/a Mon, Nov 23 2020 6:47 PM', 'Monday Mon, Nov 23 2020 7:20 PM to 8:40 PM n/a Mon, Nov 23 2020 6:08 PM', 'Monday Mon, Nov 23 2020 7:00 PM to 8:00 PM n/a Mon, Nov 23 2020 5:56 PM', 'unday Sun, Nov 22 2020 5:40 PM to 7:00 PM n/a Sun, Nov 22 2020 4:52 PM', 'unday Sun, Nov 22 2020 5:20 PM to 6:40 PM n/a Sun, Nov 22 2020 4:36 PM', 'unday Sun, Nov 22 2020 5:00 PM to 6:00 PM n/a Sun, Nov 22 2020 4:11 PM', 'unday Sun, Nov 22 2020 4:40 PM to 6:00 PM n/a Sun, Nov 22 2020 4:00 PM', 'unday Sun, Nov 22 2020 4:20 PM to 5:40 PM n/a Sun, Nov 22 2020 3:27 PM', 'unday Sun, Nov 22 2020 4:00 PM to 5:00 PM n/a Sun, Nov 22 2020 2:21 PM', 'Saturday Sat, Nov 21 2020 4:40 PM to 6:00 PM n/a Sat, Nov 21 2020 3:50 PM', 'Saturday Sat, Nov 21 2020 4:20 PM to 5:40 PM n/a Sat, Nov 21 2020 3:16 PM', 'Saturday Sat, Nov 21 2020 4:00 PM to 5:00 PM n/a Sat, Nov 21 2020 3:05 PM', 'Saturday Sat, Nov 21 2020 3:40 PM to 5:00 PM n/a Sat, Nov 21 2020 2:19 PM', 'Saturday Sat, Nov 21 2020 2:40 PM to 4:00 PM n/a Sat, Nov 21 2020 12:51 PM', 'Saturday Sat, Nov 21 2020 12:40 PM to 2:00 PM n/a Sat, Nov 21 2020 11:32 AM', 'Saturday Sat, Nov 21 2020 12:00 PM to 1:00 PM n/a Sat, Nov 21 2020 1:25 AM', 'Friday Fri, Nov 20 2020 5:00 PM to 6:00 PM n/a Fri, Nov 20 2020 4:14 PM', 'Friday Fri, Nov 20 2020 4:40 PM to 6:00 PM n/a Fri, Nov 20 2020 3:45 PM', 'Friday Fri, Nov 20 2020 4:20 PM to 5:40 PM n/a Fri, Nov 20 2020 3:12 PM', 'Friday Fri, Nov 20 2020 3:40 PM to 5:00 PM n/a Fri, Nov 20 2020 2:20 PM', 'Friday Fri, Nov 20 2020 3:00 PM to 4:00 PM n/a Fri, Nov 20 2020 12:06 PM', 'Tuesday Tue, Nov 17 2020 3:00 PM to 4:00 PM n/a Tue, Nov 17 2020 2:12 PM', 'Tuesday Tue, Nov 17 2020 2:40 PM to 4:00 PM n/a Tue, Nov 17 2020 2:02 PM', 'unday Sun, Aug 23 2020 4:00 PM to 5:00 PM n/a Sun, Nov 15 2020 3:15 PM', 'unday Sun, Aug 23 2020 3:40 PM to 5:00 PM n/a Sun, Nov 15 2020 2:12 PM', 'unday Sun, Aug 23 2020 2:40 PM to 4:00 PM n/a Sun, Nov 15 2020 1:12 PM', 'unday Sun, Aug 23 2020 1:40 PM to 3:00 PM n/a Sun, Nov 15 2020 2:32 AM', 'Saturday Sat, Nov 14 2020 4:40 PM to 6:00 PM n/a Sat, Nov 14 2020 4:02 PM', 'Saturday Sat, Nov 14 2020 4:20 PM to 5:40 PM n/a Sat, Nov 14 2020 3:32 PM', 'Saturday Sat, Nov 14 2020 4:00 PM to 5:00 PM n/a Sat, Nov 14 2020 2:58 PM', 'Saturday Sat, Nov 14 2020 3:40 PM to 5:00 PM n/a Sat, Nov 14 2020 1:40 PM', 'Saturday Sat, Nov 14 2020 3:00 PM to 4:00 PM n/a Sat, Nov 14 2020 12:59 PM', 'Saturday Sat, Nov 14 2020 2:00 PM to 3:00 PM n/a Sat, Nov 14 2020 12:20 PM', 'Saturday Sat, Nov 14 2020 1:00 PM to 2:00 PM n/a Sat, Nov 14 2020 11:07 AM', 'Saturday Sat, Nov 14 2020 11:40 AM to 1:00 PM n/a Fri, Nov 13 2020 5:08 PM', 'Saturday Sat, Nov 14 2020 9:00 AM to 10:00 AM n/a Fri, Nov 13 2020 4:35 PM', 'Friday Fri, Nov 13 2020 6:00 PM to 7:00 PM n/a Fri, Nov 13 2020 9:39 AM', 'Friday Fri, Nov 13 2020 10:00 AM to 11:00 AM n/a Fri, Nov 13 2020 3:12 AM', 'Friday Fri, Nov 13 2020 8:20 AM to 9:40 AM n/a Fri, Nov 13 2020 1:18 AM', 'Friday Fri, Nov 13 2020 7:20 AM to 8:40 AM n/a Thu, Nov 12 2020 4:18 PM', 'Friday Fri, Nov 13 2020 1:20 PM to 2:40 PM n/a Thu, Nov 12 2020 11:09 AM', 'Friday Fri, Nov 13 2020 10:20 AM to 11:40 AM n/a Thu, Nov 12 2020 11:00 AM', 'Thursday Thu, Nov 12 2020 1:20 PM to 2:40 PM n/a Tue, Nov 10 2020 8:40 PM', 'Tuesday Tue, Nov 10 2020 7:40 AM to 9:00 AM n/a Sun, Nov 8 2020 4:40 PM', 'Monday Mon, Nov 9 2020 9:20 AM to 10:40 AM n/a Sat, Nov 7 2020 7:02 PM', 'unday Sun, Nov 8 2020 11:00 AM to 12:00 PM n/a Fri, Nov 6 2020 5:06 PM', 'Saturday Sat, Nov 7 2020 9:00 AM to 10:00 AM n/a Thu, Nov 5 2020 10:29 PM']]
ta = [['6:00 AM - 7:00 AM', '46 spots available'], ['6:20 AM - 7:40 AM', '46 spots available'], ['6:40 AM - 8:00 AM', '63 spots available'], ['7:00 AM - 8:00 AM', '64 spots available'], ['7:20 AM - 8:40 AM', '68 spots available'], ['7:40 AM - 9:00 AM', '69 spots available'], ['8:00 AM - 9:00 AM', '79 spots available'], ['8:20 AM - 9:40 AM', '67 spots available'], ['8:40 AM - 10:00 AM', '73 spots available'], ['9:00 AM - 10:00 AM', '73 spots available'], ['9:20 AM - 10:40 AM', '77 spots available'], ['9:40 AM - 11:00 AM', '76 spots available'], ['10:00 AM - 11:00 AM', '84 spots available'], ['10:20 AM - 11:40 AM', '83 spots available'], ['10:40 AM - 12:00 PM', '83 spots available'], ['11:00 AM - 12:00 PM', '83 spots available'], ['11:20 AM - 12:40 PM', '87 spots available'], ['11:40 AM - 1:00 PM', '77 spots available'], ['12:00 PM - 1:00 PM', '84 spots available'], ['12:20 PM - 1:40 PM', '89 spots available'], ['12:40 PM - 2:00 PM', '85 spots available'], ['1:00 PM - 2:00 PM', '85 spots available'], ['1:20 PM - 2:40 PM', '84 spots available'], ['1:40 PM - 3:00 PM', '83 spots available'], ['2:00 PM - 3:00 PM', '89 spots available'], ['2:20 PM - 3:40 PM', '87 spots available'], ['2:40 PM - 4:00 PM', '81 spots available'], ['3:00 PM - 4:00 PM', '80 spots available'], ['3:20 PM - 4:40 PM', '73 spots available'], ['3:40 PM - 5:00 PM', '76 spots available'], ['4:00 PM - 5:00 PM', '79 spots available'], ['4:20 PM - 5:40 PM', '80 spots available'], ['4:40 PM - 6:00 PM', '77 spots available'], ['5:00 PM - 6:00 PM', '84 spots available'], ['5:20 PM - 6:40 PM', '75 spots available'], ['5:40 PM - 7:00 PM', '82 spots available'], ['6:00 PM - 7:00 PM', '84 spots available'], ['6:20 PM - 7:40 PM', '79 spots available'], ['6:40 PM - 8:00 PM', '83 spots available'], ['7:00 PM - 8:00 PM', '85 spots available'], ['7:20 PM - 8:40 PM', '83 spots available'], ['7:40 PM - 9:00 PM', '84 spots available'], ['8:00 PM - 9:00 PM', '77 spots available'], ['8:20 PM - 9:40 PM', '82 spots available'], ['8:40 PM - 10:00 PM', '81 spots available'], ['9:00 PM - 10:00 PM', '88 spots available']]


def top_k_occuring(time_slots, k = 3):
        
    # Lazy import good idea?
    from collections import Counter
    c = Counter(time_slots)
    return c.most_common(k)


def automate_today(data, moa):
    """

    Parameters
    ----------
    data : users cookies stored in class object.
    moa : array with users favorite time slots.
    
    Returns
    -------
    None.

    """
    
    data.parsed.driver.get("https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1")
    import time

    time.sleep(2)
    
    id_t = "divBookingDateSelector"    
    day_header = WebDriverWait(data.parsed.driver, 20).until(
                EC.presence_of_element_located((By.ID, id_t)))
    
    day_to_click = day_header.find_element_by_xpath("//*[@id='divBookingDateSelector']/div[2]/div[2]")
    days = day_to_click.find_elements_by_tag_name("button")
    
    
    day_array = data.days
    for item in day_array:
        if (item.isnumeric()):
            day_array.remove(item)

    print("\n\nThese are the days: {}".format(day_array))
    print ("Scanning total spots available...")
    
    days[0].click()
    time, isBooked = data.processing_data()
    
    times = gui.append_colon_zero(time)
    

    import random
    delta_idx = random.randint(0,25) # default fail-safe 
    

    
    for idx, values in enumerate(times):
        # Find this users favorite time slot, for the desired TIME and book it for all days.
        
        # IF the user forgets to turn on his script or whatever, send an email or just cancel it.
            # CANT RISK GETTING BANNED. 24 hours then 48 then fucking permanent thats insane...
            # Even mordern-day jails are more liberal.
        
        #Keep swapping it if the user doesnt cancel it, so find a nice spot say 5PM,
        #IF the user doesnt "ACCEPT" the booking, auto cancel and push back to a new spot.
        
        # THis is basically PRECOVID gym going expierence.
        # You just show up. No dumb bookings.
            # I still dont understand why I spent a month of my life building this 
        
        # ----------------------------
        # moa has the 3-4 top most favorite spots, we have a delta. just need to find least such spot,
        # book it and schdule its cancellation on a parelle processor.
        
        # The first item in moa is the earliest spot in times array, so we have an index too.
            # So that means within +/- 1 index of this just keep booking it, and cancel it and so forth.
        
        
        if (values[0] == moa[0]):
            print ("Success")
            delta_idx = idx
      
    print (delta_idx)
    print (moa)
    print (times[delta_idx])
    
    # delta_idx has the delta for the users favorite spot, now just begin booking and swapping.
  
    

def fav_day(day_array):
    """

    Parameters
    ----------
    day_array :     array containing frequency of days

    Returns
    -------
    array:          favorite day.

    """
    
    # yeah this is really stupid I forgot you could do this in python
    return max(day_array)
    

def count_mode_day(am_pm_array):
    """
    Parameters
    ----------
    am_pm_array : array containing alot of bookings which have AM/PMs in them

    Returns
    -------
    data : an array with number of AM/PMs only.
    mode : string with the actual value of AM/PM
    """
    
    am = 0
    pm = 0
    
    for elem in am_pm_array:
        
        # If you have something at AM/PM both, like 11AM-12PM its irrelevant lets just call that a border case.
        # And let it exist as whatever.
        
        if (elem.find("AM") == -1):
            pm +=1
        
        if (elem.find("PM") == -1):
            am += 1
            
    data = [am, pm]
    mode = "AM"
    if (am >= pm):
        mode = "Mornings (AM)"
    else:
        mode = "Nights (PM)"
    return data, mode

def automate(data):
    """
    Args
    ------
    data:       users session cookies

    Returns
    -------
    void
    """
    
    #user_name = gu.get_all_bookings(data, True)
    user_name = REPLACE_ME[2]

    print ("-" * 20)
    print ("Welcome, {}".format(user_name))
    print ("-" * 20)
    print ("I hope you're having a good day.")
    
    print ("-" * 20)
    print ("\nYour favorite day is: \t\t\t{}".format(fav_day(REPLACE_ME[0])))
    
    am_pm_count, mode = count_mode_day(REPLACE_ME[3])
    print ("Your preferred time of the day is: \t{}\n".format(mode))
    
    
        
    top = top_k_occuring(REPLACE_ME[3])
    
    # Array containing users favorite spots with desired time of the day.
    most_occuring_slot_array = list()
    for item in top:
        desired_val = item[0].replace('to', '-')
        clean_data = desired_val[:len(desired_val) - 1]
        most_occuring_slot_array.append(clean_data)
    
    most_occuring_slot_array.sort()
    
    print ("Your favorite spots are: ")    
    for item in most_occuring_slot_array:
        print ("\t\t\t\t\t" + item)
    
    
    # ---------------------
        # TODO
    automate_today(data, most_occuring_slot_array)
    # ---------------------
    
    print ("\n\n\n")
    print ("- " * 20)
    print ("This is currently a work in progress, check back later.\n\n")


#automate(None)