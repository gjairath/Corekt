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

def book(data, isConcurrent, times):
    user_booking = input("\nEnter the choice as indicated by the []'s: ")
                
    user_confirmation = input("\nAre you sure you want to book [{}] [Yes|No]:".format(user_booking))
    
    if (times[int(user_booking) - 1][1] == "0 spots available"):
        print ("Your spot is taken, switching to concurrent booking @ 15 requests per minute.")
        isConcurrent = True
    
    
    if (user_confirmation == "No"): return

    class_book = data.parsed.driver.find_element_by_class_name("container-flex")

    booking_card = class_book.find_element_by_xpath("(//*[@class='booking-slot-item'])[%d]" % int(user_booking))
    booking = booking_card.find_element_by_tag_name("button")
    
    if (isConcurrent == False):
           try: 
               booking.click()
               print("\nSuccess!")
           except: print ("\n\n\nSomething weird happened, your spot might have none available. \
                          \nTry concurrent booking on the main menu.\n")
           return
      

 
    if (isConcurrent == True):
        print ("\nWhen a spot opens up you'll be the first in line.\n\n")
        print ("Loading", end = "")
    
    counter = 0
    while (isConcurrent == True):

            # If the element desired is found, then click the booking button and wait for the page to refresh.
        
 
            
        status = True
        while (status):
            
            try:
                print ("\nTimes Clicked: {}".format(counter))
                #So when the page reloads, the fucking button is lost in its tracks.
                class_book = data.parsed.driver.find_element_by_class_name("container-flex")
            
                booking_card = class_book.find_element_by_xpath("(//*[@class='booking-slot-item'])[%d]" % int(user_booking))
                booking = booking_card.find_element_by_tag_name("button")
                counter += 1

                booking.click()
                
                status = False
                break
                
            except:
                #I dont know. Just sleep and hope it works out lol.
                time.sleep(0.25)
            
    
    print ("\n\nSuccess!")

def cancel(data):
    print ("Showing reservations..")
    
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
    
    from datetime import date
    import calendar
    my_date = date.today()


    
    see_all = input("\n Would you like to see only active bookings? [Yes|No]: ")

    if (see_all == "Yes" or see_all == "y" or see_all == "yes" or see_all == "Y"):
        for i in range(len(list_enabled)):
            print ("\n\nToday is {} of {}".format(calendar.day_name[my_date.weekday()], my_date) ) 
                       
            print("----------")
            print ("[" + str(i + 1) + "]", end = " ")
            
            string = list_enabled[i].text.split(",")[1].split("CANCEL")[0]
            
            match = re.match(r'.*([1-3][0-9]{3})', string)
            year = match.group(1) + "    " #for some reason this is the only way
            
            # The things you do for idiot users
            print (string.replace(match.group(1), year))
            
                  
    else:
        for i in range(len(list_disabled)):
            print ("\n\nToday is {} of {}".format(calendar.day_name[my_date.weekday()], my_date) ) 
                   
            print("----------")
            print ("[" + str(i + 1) + "]", end = " ")
            
            string = list_disabled[i].text.split(",")[1].split("CANCEL")[0]
            
            match = re.match(r'.*([1-3][0-9]{3})', string)
            year = match.group(1) + "        " #for some reason this is the only way
            
            # The things you do for idiot users
            print (string.replace(match.group(1), year))
            
            
    
    
    if (list_enabled == []): 
        print ("\nYou have no bookings. \n")
        return()
    
    user_choice = input("Enter the choice you want to cancel: ")
   
    try: enabled_click[int(user_choice) - 1].click()
    except: 
        print ("You entered something wrong, try again")
        return
 
    try:
        id_cancel = "modalCancelBooking"
        confirm_click = WebDriverWait(data.parsed.driver, 20).until(
            EC.presence_of_element_located((By.ID, id_cancel)))
        
        all_buttons = confirm_click.find_elements_by_tag_name("button")
        
        
        for item in all_buttons:
            #this is flexible, no way they will change their code base they might change the stupid text.
            if (item.get_attribute("onclick") == "CancelBooking()"):
                desired_confirmation_btn = item
            else:
                desired_confirmation_btn = all_buttons[2]
        
        # SUCH an elusive bug really, I was running this in debugger, and the selenium module works so fast,
                # That it literally clicks an element that doesnt exist and falls into except.
                # element_to_be_clickable is glitchy, I'm not sure hwy, I rather have a program thats consistent
                # than something fast
        isTrue = True
        i = 0
        while(isTrue):
            try:
                desired_confirmation_btn.click()
                
                isTrue = False
            except:
                time.sleep(0.25)
                i += 1
                print("\n\nLoading", end = "")
                print (".", end = "")
                if (i == 10): break
  
      
#        desired_confirmation_btn.click()
        
    except:
        print ("\nSomething went wrong, try again")
        return
    
    
    print ("\n\nSuccess, your booking is cancelled.\n")
    return
