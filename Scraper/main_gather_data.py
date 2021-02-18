"""
Created on Mon Feb  1 03:31:29 2021

@author: garvi

Filename: Main.py
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# This is an edit of the main progra to collect all the data from the corec site and upload it into a databse.
# To perform cooky AI stuff or just make fancy graphs.

# IT's more or less a learning expierence.


import process_data as pd
import gui_utility as gui
from sys import *
import booking_utility as bu
import time

if __name__ == "__main__":
    
    data = pd.ProcessData()
    
    is_true = True
    
    while (is_true):
        data.parsed.driver.get("https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1")
        
        time.sleep(3)
        days = data.show_days()
                                    
        id_t = "divBookingDateSelector"
        
        
        day_header = WebDriverWait(data.parsed.driver, 20).until(
                        EC.presence_of_element_located((By.ID, id_t)))

        
        day_to_click = day_header.find_element_by_xpath("//*[@id='divBookingDateSelector']/div[2]/div[2]")
        days = day_to_click.find_elements_by_tag_name("button")

        
        days[0].click()
    
        time.sleep(3)

        data.refetch_data_time()
        
        #displays the time slots.
        times, isBooked = data.processing_data() 


        times = gui.prettify(times)
        
        
        print (times)
        bu.cancel (data)
        
        attended_bookings = bu.get_all_attendance(data)
        all_bookings = bu.get_all_bookings(data)
        
        
        print ((all_bookings))
            