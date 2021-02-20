# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 01:58:31 2021

@author: garvi
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import time
import sys
import re

#Booking.utility.

'''
 element = WebDriverWait(data.parsed.driver, 20).until(
     EC.presence_of_element_located((By.ID, "divBookingSlots")))

'''


def get_all_attendance(data):
    
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#ProgramAttendance")
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#ProgramAttendance")
 #   data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#ProgramAttendance")

    notFound = True
    while(notFound):    
        try:
            arr = data.parsed.driver.find_element_by_tag_name("table").text.split("\n")
            
            notFound = False
        except:
            print ("Loading")
            print (".", end = "")
            time.sleep(0.25)


    return arr


def make_graphs_bookings(days, dates_and_times, name, am_pm, tot_arr):

    '''
    Args.
        Days: The days to show up.
        Dates: The date to show up.
        
        Date_registered: <>
            
        tot_arr: THe array with all bookings include no shows and cancellations.
    
    Returns
        The graphs lol
    '''
        

    # Lazy import.
    import pandas as pd
    import matplotlib.pyplot as plt


    l = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    df = pd.DataFrame({'freq': days})
    
    df.groupby('freq', as_index=True).size().sort_values().plot(kind='bar', orientation='vertical')
    
    plt.xticks(rotation='horizontal')
    plt.xlabel("The Days")
    plt.ylabel("Frequency/Number of Days")
    plt.title("Frequency of Days Showed for {}".format(name))
    plt.tight_layout()

    plt.show()
    
    
    # Graph of a pie chart showing what days the bookings were mostly booked.
    
    explode=(0.12, 0.12, 0.12, 0.12, 0.12, 0.12)
    df.value_counts().plot(kind='pie', labels = l, title = "Pie Chart for Days Booked {}".format(name), \
                          shadow = True, autopct='%1.1f%%', ylabel = "", explode = explode, pctdistance=0.65)
    plt.tight_layout()        
    plt.show()
    
    
    dates = dates_and_times
    
    
    # Graph to show a bar plot of the dates the reserations were booked.
    df = pd.DataFrame({'freq': dates})
    
    df.groupby('freq', as_index=True).size().sort_values().plot(kind='bar', orientation='vertical')
    
    plt.xlabel("The Days")
    plt.ylabel("Frequency/Number of Days")
    plt.title("Frequency of Days Showed {}".format(name))
    plt.tight_layout()
    
    plt.show()
    
    
    
    # Graph to show a scatter plot of the dates it was mostly booked.
    
    import seaborn as sns
    from collections import Counter
    
    counter = Counter(dates)
    df_new = pd.DataFrame.from_dict(counter, orient='index').reset_index()
    
    
    g = sns.scatterplot(x = 'index', y = 0, data = df_new)
    g.set_xticklabels(rotation=90, labels = df_new['index'])
    plt.tight_layout()
    
    plt.show()
    
    
    
    # Graph to show the pie chart of when the person books for showing up, AM/PMs.
    am = 0
    pm = 0
    
    for elem in am_pm:
        
        # If you have something at AM/PM both, like 11AM-12PM its irrelevant lets just call that a border case.
        # And let it exist as whatever.
        
        if (elem.find("AM") == -1):
            pm +=1
        
        if (elem.find("PM") == -1):
            am += 1
            
    data = [am, pm]
    labels = ['AM', 'PM']
    explode = (0.1, 0.1)
    plt.pie(data, labels = labels, shadow = True, autopct='%1.1f%%', explode = explode, pctdistance=0.65) 
    plt.tight_layout()
    plt.show() 


    return

    

def get_all_bookings(data):
    # Program to fidn total bookings.
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#Reg")
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#Reg")
    
    
    # either the page is fucked or something with the pages array, it works in GDB.
    
    time.sleep(3)
    
    lower_scroll = data.parsed.driver.find_elements_by_tag_name("tfoot")
    pages = lower_scroll[0].find_elements_by_tag_name("a")
    
    # IF a user has 10 pages worth of bookigns, 10 pages + 1 for the forward button.
    # ARrays start at 0 ahhaha good joke memes programming humor. 
    
    total_array = []
    counter_loop = 0
    for i in range(len(pages)):       
        time.sleep(3)
        lower_scroll = data.parsed.driver.find_elements_by_tag_name("tfoot")
        pages = lower_scroll[0].find_elements_by_tag_name("a")
        forward_button = pages[len(pages) - 1] 

    
        string = data.parsed.driver.find_element_by_id("content_Reg").text    
        find = string.find("CoRec Access")    
        new_string = string[find:] # The relevant data, with trash filtered out.
        
        # Either the booking is paid or cancelled.
        # Thus, just split it at that point.
        
        new_string = new_string.replace("\nCancelled", "\nPaid")
        arr = new_string.split("\nPaid")
        
        if (arr[len(arr) - 1] == ""):
            del arr[len(arr) - 1]
        
        total_array.extend(arr)
        
        isClick = True
        while(isClick and i != len(pages) - 1 and counter_loop <= len(pages)):
            try:
                pages[counter_loop].click()
                if (i == 0): counter_loop += 1
                isClick = False
                
            except:
                time.sleep(0.25)
                print ("Loading..")
                
        counter_loop += 1
    
    days_frequently_booked = []
    date_time_array = []
    
    am_pm_instances = []
    
    name = total_array[1].split(" ")[0]    
    for idx, sub_rows in enumerate(total_array):

        length = sub_rows.find("Reservation:") + 13
        total_array[idx] = sub_rows[length:]
        
        splits = total_array[idx].split("n/a")
        
        
        # THis is done on purpose btw im really smart i would like to say.
        day_booked = splits[0]
        day = day_booked.split(" ")[0]
        
        # For some reason the website acts up with a sunday.
        if (day == "unday"): day = "Sunday"
        days_frequently_booked.append(day)
                
        lf = day_booked.split(",")[1].split(" ")[1:4]
        joiner = " "
        
        lf2 = day_booked.split(",")[1].split(" ")[4:]

        date_time_array.append(joiner.join(lf))
        
        am_pm_instances.append(joiner.join(lf2))
        
    make_graphs_bookings(days_frequently_booked, date_time_array, name, am_pm_instances, total_array)
    return total_array                


def cancel(data):
    
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#CourtBook")
    


    class_cancel = WebDriverWait(data.parsed.driver, 20).until(
            EC.presence_of_element_located((By.ID, "content_CourtBook")))
    
    try: inner_class = class_cancel.find_element_by_class_name("panel-default")
    except: inner_class = class_cancel
    
    i = 0
    isTrue = True
    #G is a shit name but its basically the entire table content.
    while(isTrue):
        try:
            g = inner_class.find_element_by_tag_name("table")
            isTrue = False
        except:
            time.sleep(0.25)
            print("\n\nLoading", end = "")
            print (".", end = "")
            i += 1
            if (i == 5):
                isTrue = False
                print ("Something went wrong, try again")
                return
    
    # l  is the element 1 layer down.
    ir = g.find_element_by_tag_name("tbody")
    
    # total number of elements, some are disabled.
    size_of_list = len(ir.text.split("\n"))
    
    list_enabled = []
    list_disabled = []
    
    enabled_click = []
    
    for i in range(size_of_list):
        # These are the rows of all th bookings, some are expired. 
        
        #If a person has made 15 bookings, there are 15 rows, each have like 
        if (i==size_of_list): break
    
        
        try: row = ir.find_elements_by_tag_name("tr")[i]
        except: pass
        #this is a bad name for a var but I need the additional clarity
        # it contains name, day, time, in the form of webdrivers that each have it or someting idfk.
        
        # This is a list of 4 WebDriver instances, each have use, name, date, day and cancel.
        #inner_cell_values_of_bookings = row.find_element_by_tag_name("button")
        
        
        # The thid value is CANCEL. Go one laye down to the button and exampline this value.
        #btn_cancel = inner_cell_values_of_bookings[3].find_element_by_tag_name("button")
        is_cancel_exist = True
        row_stuff = row.find_elements_by_tag_name("td")[3]
        if (row_stuff.text == "" or row_stuff.text == ''): 
            is_cancel_exist = False
            
        if (is_cancel_exist): cancel_btn = row.find_element_by_tag_name("button")
    
        
        if (is_cancel_exist == True or is_cancel_exist == "True"):
            list_enabled.append(row)
            enabled_click.append(cancel_btn)
        else:
            list_disabled.append(row)
            
            
            
    for i in range(len(list_disabled)):                      
            print("----------")
            print ("[" + str(i + 1) + "]", end = " ")
            
            string = list_disabled[i].text.split(",")[1].split("CANCEL")[0]
            
            match = re.match(r'.*([1-3][0-9]{3})', string)
            year = match.group(1) + "        " #for some reason this is the only way
            
            # The things you do for idiot users
            print (string.replace(match.group(1), year))
            
            
    return
