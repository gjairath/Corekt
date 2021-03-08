# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 00:10:27 2021

@author: garvi
"""


# automate_utility.py

import graph_utility as gu


REPLACE_ME = [['Tuesday', 'Monday', 'Monday', 'Monday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Friday', 'Friday', 'Friday', 'Friday', 'Friday', 'Tuesday', 'Tuesday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Saturday', 'Friday', 'Friday', 'Friday', 'Friday', 'Friday', 'Friday', 'Thursday', 'Tuesday', 'Monday', 'Sunday', 'Saturday'], ['Nov 24 2020', 'Nov 23 2020', 'Nov 23 2020', 'Nov 23 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 17 2020', 'Nov 17 2020', 'Aug 23 2020', 'Aug 23 2020', 'Aug 23 2020', 'Aug 23 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 12 2020', 'Nov 10 2020', 'Nov 9 2020', 'Nov 8 2020', 'Nov 7 2020'], '\nGarvit', ['5:00 PM to 6:00 PM ', '7:40 PM to 9:00 PM ', '7:20 PM to 8:40 PM ', '7:00 PM to 8:00 PM ', '5:40 PM to 7:00 PM ', '5:20 PM to 6:40 PM ', '5:00 PM to 6:00 PM ', '4:40 PM to 6:00 PM ', '4:20 PM to 5:40 PM ', '4:00 PM to 5:00 PM ', '4:40 PM to 6:00 PM ', '4:20 PM to 5:40 PM ', '4:00 PM to 5:00 PM ', '3:40 PM to 5:00 PM ', '2:40 PM to 4:00 PM ', '12:40 PM to 2:00 PM ', '12:00 PM to 1:00 PM ', '5:00 PM to 6:00 PM ', '4:40 PM to 6:00 PM ', '4:20 PM to 5:40 PM ', '3:40 PM to 5:00 PM ', '3:00 PM to 4:00 PM ', '3:00 PM to 4:00 PM ', '2:40 PM to 4:00 PM ', '4:00 PM to 5:00 PM ', '3:40 PM to 5:00 PM ', '2:40 PM to 4:00 PM ', '1:40 PM to 3:00 PM ', '4:40 PM to 6:00 PM ', '4:20 PM to 5:40 PM ', '4:00 PM to 5:00 PM ', '3:40 PM to 5:00 PM ', '3:00 PM to 4:00 PM ', '2:00 PM to 3:00 PM ', '1:00 PM to 2:00 PM ', '11:40 AM to 1:00 PM ', '9:00 AM to 10:00 AM ', '6:00 PM to 7:00 PM ', '10:00 AM to 11:00 AM ', '8:20 AM to 9:40 AM ', '7:20 AM to 8:40 AM ', '1:20 PM to 2:40 PM ', '10:20 AM to 11:40 AM ', '1:20 PM to 2:40 PM ', '7:40 AM to 9:00 AM ', '9:20 AM to 10:40 AM ', '11:00 AM to 12:00 PM ', '9:00 AM to 10:00 AM '], ['Tuesday Tue, Nov 24 2020 5:00 PM to 6:00 PM n/a Tue, Nov 24 2020 3:16 PM', 'Monday Mon, Nov 23 2020 7:40 PM to 9:00 PM n/a Mon, Nov 23 2020 6:47 PM', 'Monday Mon, Nov 23 2020 7:20 PM to 8:40 PM n/a Mon, Nov 23 2020 6:08 PM', 'Monday Mon, Nov 23 2020 7:00 PM to 8:00 PM n/a Mon, Nov 23 2020 5:56 PM', 'unday Sun, Nov 22 2020 5:40 PM to 7:00 PM n/a Sun, Nov 22 2020 4:52 PM', 'unday Sun, Nov 22 2020 5:20 PM to 6:40 PM n/a Sun, Nov 22 2020 4:36 PM', 'unday Sun, Nov 22 2020 5:00 PM to 6:00 PM n/a Sun, Nov 22 2020 4:11 PM', 'unday Sun, Nov 22 2020 4:40 PM to 6:00 PM n/a Sun, Nov 22 2020 4:00 PM', 'unday Sun, Nov 22 2020 4:20 PM to 5:40 PM n/a Sun, Nov 22 2020 3:27 PM', 'unday Sun, Nov 22 2020 4:00 PM to 5:00 PM n/a Sun, Nov 22 2020 2:21 PM', 'Saturday Sat, Nov 21 2020 4:40 PM to 6:00 PM n/a Sat, Nov 21 2020 3:50 PM', 'Saturday Sat, Nov 21 2020 4:20 PM to 5:40 PM n/a Sat, Nov 21 2020 3:16 PM', 'Saturday Sat, Nov 21 2020 4:00 PM to 5:00 PM n/a Sat, Nov 21 2020 3:05 PM', 'Saturday Sat, Nov 21 2020 3:40 PM to 5:00 PM n/a Sat, Nov 21 2020 2:19 PM', 'Saturday Sat, Nov 21 2020 2:40 PM to 4:00 PM n/a Sat, Nov 21 2020 12:51 PM', 'Saturday Sat, Nov 21 2020 12:40 PM to 2:00 PM n/a Sat, Nov 21 2020 11:32 AM', 'Saturday Sat, Nov 21 2020 12:00 PM to 1:00 PM n/a Sat, Nov 21 2020 1:25 AM', 'Friday Fri, Nov 20 2020 5:00 PM to 6:00 PM n/a Fri, Nov 20 2020 4:14 PM', 'Friday Fri, Nov 20 2020 4:40 PM to 6:00 PM n/a Fri, Nov 20 2020 3:45 PM', 'Friday Fri, Nov 20 2020 4:20 PM to 5:40 PM n/a Fri, Nov 20 2020 3:12 PM', 'Friday Fri, Nov 20 2020 3:40 PM to 5:00 PM n/a Fri, Nov 20 2020 2:20 PM', 'Friday Fri, Nov 20 2020 3:00 PM to 4:00 PM n/a Fri, Nov 20 2020 12:06 PM', 'Tuesday Tue, Nov 17 2020 3:00 PM to 4:00 PM n/a Tue, Nov 17 2020 2:12 PM', 'Tuesday Tue, Nov 17 2020 2:40 PM to 4:00 PM n/a Tue, Nov 17 2020 2:02 PM', 'unday Sun, Aug 23 2020 4:00 PM to 5:00 PM n/a Sun, Nov 15 2020 3:15 PM', 'unday Sun, Aug 23 2020 3:40 PM to 5:00 PM n/a Sun, Nov 15 2020 2:12 PM', 'unday Sun, Aug 23 2020 2:40 PM to 4:00 PM n/a Sun, Nov 15 2020 1:12 PM', 'unday Sun, Aug 23 2020 1:40 PM to 3:00 PM n/a Sun, Nov 15 2020 2:32 AM', 'Saturday Sat, Nov 14 2020 4:40 PM to 6:00 PM n/a Sat, Nov 14 2020 4:02 PM', 'Saturday Sat, Nov 14 2020 4:20 PM to 5:40 PM n/a Sat, Nov 14 2020 3:32 PM', 'Saturday Sat, Nov 14 2020 4:00 PM to 5:00 PM n/a Sat, Nov 14 2020 2:58 PM', 'Saturday Sat, Nov 14 2020 3:40 PM to 5:00 PM n/a Sat, Nov 14 2020 1:40 PM', 'Saturday Sat, Nov 14 2020 3:00 PM to 4:00 PM n/a Sat, Nov 14 2020 12:59 PM', 'Saturday Sat, Nov 14 2020 2:00 PM to 3:00 PM n/a Sat, Nov 14 2020 12:20 PM', 'Saturday Sat, Nov 14 2020 1:00 PM to 2:00 PM n/a Sat, Nov 14 2020 11:07 AM', 'Saturday Sat, Nov 14 2020 11:40 AM to 1:00 PM n/a Fri, Nov 13 2020 5:08 PM', 'Saturday Sat, Nov 14 2020 9:00 AM to 10:00 AM n/a Fri, Nov 13 2020 4:35 PM', 'Friday Fri, Nov 13 2020 6:00 PM to 7:00 PM n/a Fri, Nov 13 2020 9:39 AM', 'Friday Fri, Nov 13 2020 10:00 AM to 11:00 AM n/a Fri, Nov 13 2020 3:12 AM', 'Friday Fri, Nov 13 2020 8:20 AM to 9:40 AM n/a Fri, Nov 13 2020 1:18 AM', 'Friday Fri, Nov 13 2020 7:20 AM to 8:40 AM n/a Thu, Nov 12 2020 4:18 PM', 'Friday Fri, Nov 13 2020 1:20 PM to 2:40 PM n/a Thu, Nov 12 2020 11:09 AM', 'Friday Fri, Nov 13 2020 10:20 AM to 11:40 AM n/a Thu, Nov 12 2020 11:00 AM', 'Thursday Thu, Nov 12 2020 1:20 PM to 2:40 PM n/a Tue, Nov 10 2020 8:40 PM', 'Tuesday Tue, Nov 10 2020 7:40 AM to 9:00 AM n/a Sun, Nov 8 2020 4:40 PM', 'Monday Mon, Nov 9 2020 9:20 AM to 10:40 AM n/a Sat, Nov 7 2020 7:02 PM', 'unday Sun, Nov 8 2020 11:00 AM to 12:00 PM n/a Fri, Nov 6 2020 5:06 PM', 'Saturday Sat, Nov 7 2020 9:00 AM to 10:00 AM n/a Thu, Nov 5 2020 10:29 PM']]

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
    print ("I hope you're having a good day.\n")
    
    print ("-" * 20)
    print ("Your favorite day is: {}\n".format(fav_day(REPLACE_ME[0])))
    
    am_pm_count, mode = count_mode_day(REPLACE_ME[3])
    print ("Your preferred time of the day is: {}\n".format(mode))
    
    
    
    print ("\n\nThis is currently a work in progress, check back later.\n\n")


automate(None)