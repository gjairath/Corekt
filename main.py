# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 03:31:29 2021

@author: garvi

Filename: Main.py
"""


import process_data as pd
import gui_utility as gui
from sys import *
import booking_utility as bu
import time

if __name__ == "__main__":
    
    data = pd.ProcessData()
    
    is_true = True
    
    while (is_true):
        
        user_decision = input("\n[[1] Book | [2] Cancel/View | [3] Quit]: ")
        
        if (user_decision == "1"):
            
            data.parsed.driver.get("https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1")
        
            days = data.show_days()
            
            choice = input("\n\nWhat Day? Enter numerically. \n q to quit: ")    
        
        
            if (choice == "q" or choice == "Q"): 
                is_true = False
                print ("Exiting...")
                exit()
                
            time.sleep(4)    
       
            day_to_click  = data.parsed.driver.find_element_by_xpath(
                          "/html/body/div[5]/div[1]/div[2]/div[9]/div[2]/div[2]/button[%d]" % int(choice))
            
            day_to_click.click()
        
            
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
                    bu.book(data)
                    
            if (show_all == "Book" or show_all == "book" or show_all == "b" or show_all == "B"):
                
                if (isBooked):
                    print ("You've already booked on this day, cancel and try again.")
                else:    
                    bu.book(data)
        
        elif (user_decision == "2"):
            bu.cancel(data)
            
        
        else:
            exit()