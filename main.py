# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 03:31:29 2021

@author: garvi

Filename: Main.py
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import process_data as pd
import gui_utility as gui
from sys import *
import booking_utility as bu
import time

if __name__ == "__main__":
    
    data = pd.ProcessData()
    
    is_true = True
    
    while (is_true):
        
        user_decision = input("\n[[1] Book | [2] Cancel/View | [3] Concurrent-Booking \
                                \n[4] Auto-Book/Cancel The Least Spot | [5] Quit |]: ")
        
        if (user_decision == "1" or user_decision == "3"):
            
            data.parsed.driver.get("https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1")
        
            days = data.show_days()
            
            choice = input("\n\nWhat Day? Enter numerically [1,2,3]. \n q to quit: ")    
            
            if (choice == ""): choice = "1"
            
            if (choice == "q" or choice == "Q"): 
                is_true = False
                print ("Exiting...")
                exit()
                
            id_t = "divBookingDateSelector"
            
            day_header = WebDriverWait(data.parsed.driver, 20).until(
                            EC.presence_of_element_located((By.ID, id_t)))

            
            day_to_click = day_header.find_element_by_xpath("//*[@id='divBookingDateSelector']/div[2]/div[2]")
            days = day_to_click.find_elements_by_tag_name("button")

            
            days[int(choice)].click()
        
            
            if (choice != 1): data.refetch_data_time()
            
            #displays the time slots.
            times, isBooked = data.processing_data() 


            gui.prettify(times, days, choice)
            
            show_all = input("===============\n\n See all options? [Yes|No (Go Back)|Book]: ")
            if (show_all == "Yes"): 
                for idx in range(len(times)):
                    print("[" + str(idx + 1) + "] " + times[idx][0] + "\t\t\t" + times[idx][1])
                
                if (isBooked):
                    print ("You've already booked on this day, cancel and try again.")
                
                else:
                    bu.book(data, False, times)
                    
            if (show_all == "Book" or show_all == "book" or show_all == "b" or show_all == "B"):
                
                if (isBooked):
                    print ("You've already booked on this day, cancel and try again.")
                else:    
                    isConcurrent = False
                    if (user_decision == "3"): isConcurrent = True
                    bu.book(data, isConcurrent, times)
        
        elif (user_decision == "2"):
            bu.cancel(data)
            
        
        elif (user_decision == "4"):
            data.parsed.driver.get("https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1")
        
            days = data.show_days()
            
            choice = input("\n\nWhat Day? Enter numerically [1,2,3]. \n q to quit: ")    
            
            if (choice == ""): choice = "1"
            
            if (choice == "q" or choice == "Q"): 
                is_true = False
                print ("Exiting...")
                exit()
                
            x = "/html/body/div[5]/div[1]/div[2]/div[9]/div[2]/div[2]/button[%d]" % int(choice)
            day_to_click = WebDriverWait(data.parsed.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, x)))
 
            day_to_click.click()
        
            
            if (choice != 1): data.refetch_data_time()
            
            #displays the time slots.
            times, isBooked = data.processing_data() 
            
            
            
            all_spots = list()
            for item in times:
                spots = int(item[1][0])
                all_spots.append(spots)
                
            desired_val = min(i for i in all_spots if i > 0)
            desired_idx = all_spots.index(desired_val)
            
            print ("Trying to book spot {} with availability {} and will cancel 15 minutes prior."
                   .format(times[desired_idx][0], times[desired_idx][1]))
            
            booking  = data.parsed.driver.find_element_by_xpath(
                "/html/body/div[5]/div[1]/div[2]/div[11]/div/div[%d]/div/button" % (desired_idx + 1))
            
            booking.click()

                    
        else:
            exit()