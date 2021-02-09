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

def book(data, isConcurrent):
    user_booking = input("\nEnter the choice as indicated by the []'s: ")
                
    user_confirmation = input("\nAre you sure you want to book [{}] [Yes|No]:".format(user_booking))
    
    if (user_confirmation == "No"): return

    booking  = data.parsed.driver.find_element_by_xpath(
        "/html/body/div[5]/div[1]/div[2]/div[11]/div/div[%d]/div/button" % int(user_booking))
  
    if (isConcurrent == False):
           booking.click()
 
    
    while (isConcurrent == True):

            # If the element desired is found, then click the booking button and wait for the page to refresh.
        
        element = WebDriverWait(data.parsed.driver, 20).until(
            EC.presence_of_element_located((By.ID, "divBookingSlots")))
        
        try:
            
            #So when the page reloads, the fucking button is lost in its tracks.
            booking  = data.parsed.driver.find_element_by_xpath(
                "/html/body/div[5]/div[1]/div[2]/div[11]/div/div[%d]/div/button" % int(user_booking))
            booking.click()
            
        except:
            #I dont know. Just sleep and hope it works out lol.
            time.sleep(2)
                
        escape_clause = data.parsed.driver.find_element_by_xpath(
            "/html/body/div[5]/div[1]/div[2]/div[11]/div[1]")
        
        if (escape_clause.text == "Some times may be unavailable due to conflicting appointments."):
            isConcurrent = False
            

def cancel(data):
    print ("Showing reservations..")
    
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#CourtBook")
    

    time.sleep(2)

    #G is a shit name but its basically the entire table content.
    g = data.parsed.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[5]/div/div/div[7]/form/div/div[2]/div[2]/table")    
    
    # l  is the element 1 layer down.
    l = g.find_element_by_tag_name("tbody")
    
    # total number of elements, some are disabled.
    size_of_list = len(l.text.split("\n"))
    
    list_enabled = []
    list_disabled = []
    
    enabled_click = []
    
    for i in range(size_of_list):
        # These are the rows of all th bookings, some are expired. 
        
        #If a person has made 15 bookings, there are 15 rows, each have like 
        
        row = l.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[5]/div/div/div[7]/form/div/div[2]/div[2]/table/tbody/tr[%d]" % int(i+1))
        #this is a bad name for a var but I need the additional clarity
        # it contains name, day, time, in the form of webdrivers that each have it or someting idfk.
        
        # This is a list of 4 WebDriver instances, each have use, name, date, day and cancel.
        inner_cell_values_of_bookings = row.find_elements_by_tag_name("td")
        
        
        # The thid value is CANCEL. Go one laye down to the button and exampline this value.
        btn_cancel = inner_cell_values_of_bookings[3].find_element_by_tag_name("button")
        is_enabled = btn_cancel.get_attribute("data-booking-cancel")
        
        if (is_enabled == "True"):
            list_enabled.append(row)
            enabled_click.append(btn_cancel)
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
            
            return
    
    
    if (list_enabled == []): 
        print ("Bro, no bookings Wtf? go get gains!")
        return()
    
    user_choice = input("Enter the choice you want to cancel: ")
   
    time.sleep(5)
   # print(enabled_click)
    enabled_click[int(user_choice) - 1].click()
    
    time.sleep(5)    
    confirm_click = data.parsed.driver.find_element_by_xpath(
        "/html/body/div[5]/div[1]/div[2]/div[5]/div/div/div[7]/form/div/div[1]/div/div/div[3]/button[2]")
    confirm_click.click()
    
    return
