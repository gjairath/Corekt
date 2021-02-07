# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 01:58:31 2021

@author: garvi
"""
from selenium.webdriver.common.by import By


#Booking.utility.

def book(data):
    user_booking = input("\nEnter the choice as indicated by the []'s: ")
                
    user_confirmation = input("\nAre you sure you want to book [{}] [Yes|No]:".format(user_booking))
    
    if (user_confirmation == "No"): return

    booking  = data.parsed.driver.find_element_by_xpath(
        "/html/body/div[5]/div[1]/div[2]/div[11]/div/div[%d]/div/button" % int(user_booking))
    
    booking.click()
    

def cancel(data):
    print ("Showing reservations..")
    
    data.parsed.driver.get("https://recwell.purdue.edu/MemberDetails#CourtBook")
    

    #G is a shit name but its basically the entire table content.
    g = data.parsed.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[5]/div/div/div[7]/form/div/div[2]/div[2]/table")    
    
    # l  is the element 1 layer down.
    l = g.find_element_by_tag_name("tbody")
    
    # total number of elements, some are disabled.
    size_of_list = len(l.text.split("\n"))
    
    list_enabled = []
    list_disabled = []
    for i in range(size_of_list):
        # These are the rows of all th bookings, some are expired. 
        
        #If a person has made 15 bookings, there are 15 rows, each have like 
        
        row = l.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[5]/div/div/div[7]/form/div/div[2]/div[2]/table/tbody/tr[%d]" % int(i+1))
        #this is a bad name for a var but I need the additional clarity
        # it contains name, day, time, in the form of webdrivers that each have it or someting idfk.
        
        # This is a list of 4 WebDriver instances, each have use, name, date, day and cancel.
        inner_cell_values_of_bookings = row.find_elements_by_tag_name("td")
        
        
        # The thid value is CANCEL. Go one laye down to the button and exampline this value.
        is_enabled = inner_cell_values_of_bookings[3].find_element_by_tag_name("button").get_attribute("data-booking-cancel")
        
        if (is_enabled == "True"):
            list_enabled.append(row)
        else:
            list_disabled.append(row)
    
    
    see_all = input("\n Would you like to see only active bookings? [Yes|No]: ")

    for i in range(len(list_enabled)):
                   
        print("----------")
        print ("\t[" + str(i + 1) + "]")
        print(list_enabled[i].text)
        
    return
