# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 03:31:29 2021

@author: garvi

Filename: Main.py
"""


import process_data as pd
import gui_utility as gui

if __name__ == "__main__":
    
    data = pd.ProcessData()
    
    is_true = True
    
    while (is_true):
        days = data.show_days()
        choice = input("\n\nEnter numerically 1 -> n (For speed purposes)\n 69 to quit:")    
    
    
        if (choice == 69): 
            is_true = False
            print ("Exiting...")
            exit()
   
        day_to_click  = data.parsed.driver.find_element_by_xpath(
                      "/html/body/div[5]/div[1]/div[2]/div[9]/div[2]/div[2]/button[%d]" % int(choice))
        
        day_to_click.click()
    
        
        if (choice != 1): data.refetch_data_time()
        
        #displays the time slots.
        times = data.processing_data() 
        
        gui.prettify(times, days, choice)
        
        show_all = input("===============\n\nWould you like to see all options instead? :[Yes|No|Book] \t")
        if (show_all == "Yes"): 
            for idx in range(len(times)):
                print("[" + str(idx + 1) + "] " + times[idx][0] + "\t\t\t" + times[idx][1])
                
                
        if (show_all == "Book" or show_all == "book" or show_all == "b" or show_all == "B"):
            user_booking = input("\nEnter the choice as indicated by the []'s: ")
                        
            user_confirmation = input("\nAre you sure you want to book [{}] [Yes|No]:".format(user_booking))
            
            if (user_confirmation == "No"): break
        
            booking  = data.parsed.driver.find_element_by_xpath(
                "/html/body/div[5]/div[1]/div[2]/div[11]/div/div[%d]/div/button" % int(user_booking))
            
            booking.click()
            
            

            