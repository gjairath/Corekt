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
    forward_button = pages[len(pages) - 1] 
    
    total_array = []

    for i in range(len(pages)):       
        
        lower_scroll = data.parsed.driver.find_elements_by_tag_name("tfoot")
        pages = lower_scroll[0].find_elements_by_tag_name("a")

    
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
        while(isClick):
            try:
                pages[i].click()
                isClick = False
            except:
                time.sleep(0.25)
                print ("Loading..")
    
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