# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 03:31:29 2021

@author: garvi

Filename: Main.py
"""


import process_data as pd

if __name__ == "__main__":
    
    data = pd.ProcessData()
    data.show_days()
        
    choice = input("\n\nEnter numerically 1 -> n (For speed purposes):")


    day_to_click  = data.parsed.driver.find_element_by_xpath(
                  "/html/body/div[5]/div[1]/div[2]/div[9]/div[2]/div[2]/button[choice")
    
    day_to_click.click()

    
