# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 03:31:29 2021

@author: garvi

Filename: Main.py
"""


import process_data as pd
import gui_utility as gu

if __name__ == "__main__":
    
    data = pd.ProcessData()
    data.show_days()
    
    is_true = True
    
    while (is_true):
        choice = input("\n\nEnter numerically 1 -> n (For speed purposes)\n 69 to quit:")    
    
    
        if (choice == 69): is_true = False
   
        day_to_click  = data.parsed.driver.find_element_by_xpath(
                      "/html/body/div[5]/div[1]/div[2]/div[9]/div[2]/div[2]/button[%d]" % int(choice))
        
        day_to_click.click()
    
        
        if (choice != 1): data.refetch_data_time()
        
        #displays the time slots.
        times = data.processing_data() 
        
        gu.prettify(times)
        
        
