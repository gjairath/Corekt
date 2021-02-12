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
           booking.click()
 
    if (isConcurrent == True):
        print ("\nWhen a spot opens up you'll be the first in line.\n\n")
        print ("Loading", end = "")
    
    counter = 0
    while (isConcurrent == True):

            # If the element desired is found, then click the booking button and wait for the page to refresh.
        
        
        if (counter == 15):
            # Sleep 30 seconds once you hit every multiple of 15 in terms of requests lmao.
            # CAnt be risked getting banned you know.
            
            time.sleep(30)
            counter = 0
            print (".")
        
        try:
            
            #So when the page reloads, the fucking button is lost in its tracks.
            booking  = data.parsed.driver.find_element_by_xpath(
                "/html/body/div[5]/div[1]/div[2]/div[11]/div/div[%d]/div/button" % int(user_booking))
            booking.click()
            counter += 1
            
        except:
            #I dont know. Just sleep and hope it works out lol.
            time.sleep(2)
            

        element = WebDriverWait(data.parsed.driver, 20).until(
            EC.presence_of_element_located((By.ID, "divBookingSlots")))
        
        
        e_text = element.text.split("\n")[0]
        
        if (e_text == "Some times may be unavailable due to conflicting appointments."):
            isConcurrent = False
            
    
    print ("\nSuccess!")

def cancel(data):
    print ("Showing reservations..")
    
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#CourtBook")
    

    
    class_cancel = WebDriverWait(data.parsed.driver, 20).until(
            EC.presence_of_element_located((By.ID, "content_CourtBook")))
    
    try: inner_class = class_cancel.find_element_by_class_name("panel-default")
    except: inner_class = class_cancel
    
    #G is a shit name but its basically the entire table content.
    g = inner_class.find_element_by_tag_name("table")
    
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
        
        row = ir.find_elements_by_tag_name("tr")[i]
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
    
        is_enabled = cancel_btn.get_attribute("onclick") #For added good measure.
        
        if (is_enabled == "ConfirmCancelParticipant(this)"):
            list_enabled.append(row)
            enabled_click.append(cancel_btn)
        else:
            list_disabled.append(row)
    
    
    see_all = input("\n Would you like to see only active bookings? [Yes|No]: ")

    if (see_all == "Yes" or see_all == "y" or see_all == "yes" or see_all == "Y"):
        for i in range(len(list_enabled)):
                       
            print("----------")
            print ("[" + str(i + 1) + "]", end = " ")
            
            string = list_enabled[i].text.split(",")[1].split("CANCEL")[0]
            
            match = re.match(r'.*([1-3][0-9]{3})', string)
            year = match.group(1) + "    " #for some reason this is the only way
            
            # The things you do for idiot users
            print (string.replace(match.group(1), year))
            
                  
    else:
        for i in range(len(list_disabled)):
                       
            print("----------")
            print ("[" + str(i + 1) + "]", end = " ")
            
            string = list_disabled[i].text.split(",")[1].split("CANCEL")[0]
            
            match = re.match(r'.*([1-3][0-9]{3})', string)
            year = match.group(1) + "        " #for some reason this is the only way
            
            # The things you do for idiot users
            print (string.replace(match.group(1), year))
            
            
    
    
    if (list_enabled == []): 
        print ("Bro, no bookings Wtf? go get gains!")
        return()
    
    user_choice = input("Enter the choice you want to cancel: ")
   
    time.sleep(2) #for good measure.
    enabled_click[int(user_choice) - 1].click()


    x = "/html/body/div[5]/div[1]/div[2]/div[5]/div/div/div[7]/form/div/div[1]/div/div/div[3]/button[2]"
 
    try:
        confirm_click = WebDriverWait(data.parsed.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, x)))
        
    except:
        print ("Something went wrong, try again")
        return

#    time.sleep(3)
   # print(enabled_click)
    
 #   time.sleep(3)    
    confirm_click.click()
    
    print ("\nSuccess, your booking is cancelled.")
    return
