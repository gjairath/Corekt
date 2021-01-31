# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 01:29:13 2021

@author: garvi
"""



# The BS object is being redirected to another link.
# Since Purdue uses CAS, I will have to login in to the main site and then redirect the bot
# To recwell to scrape relevant data.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime

#URL_scrape = "https://recwell.purdue.edu/"
URL_scrape = "https://recwell.purdue.edu/Account/Login?ReturnUrl=%2Fbooking%2F83456ef4-1d99-4e58-8e66-eb049941f7c1"
URL_login = "https://www.purdue.edu/apps/account/cas/login?service=https%3A%2F%2Fwl.mypurdue.purdue.edu"

#https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1

def site_login():
    driver.get (URL_login)
    driver.find_element_by_id("username").send_keys("gjairath")
    driver.find_element_by_id ("password").send_keys("5357,769352")
    
    submit_btn = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/form/fieldset/div[3]/div[2]/input[4]")

    # Once the button is found, click it.
    submit_btn.click()
    
    
def redirect_scrape():
    driver.get(URL_scrape)
    
    # wait for presence of divLoginOptions
    try:
        element_present = EC.presence_of_element_located((By.ID, "divLoginOptions"))
        WebDriverWait(driver, 50).until(element_present);
    except TimeoutException:
        print ("Something went wrong.")
        
    print (element_present)
    

    time.sleep(5)
    
    
    redirect_btn = driver.find_element_by_xpath(
            "/html/body/div[5]/div[4]/div/div/div/div[2]/div[2]/div[2]/div/button")        
    redirect_btn.click()
    
    driver.find_element_by_id("username").send_keys("gjairath")
    driver.find_element_by_id ("password").send_keys("5357,push")
        
    submit_btn = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/form/fieldset/div[3]/div[2]/input[4]")
    
    # Once the button is found, click it.
    submit_btn.click()



def retrieve_data():
    # flex-center margin-top-24 len is the number of available days.
    # booking-slot-item are the various "cards" that have times.
 
    data_days = driver.find_element_by_id("divBookingDateSelector")
    data_time_slots = driver.find_element_by_id("divBookingSlots")
    
    time.sleep(5)
    
    print(data_days.text)
    print(data_time_slots.text)
    
    return data_days, data_time_slots
    
    
    # Figure out how to get the main div that has all the relevant data, and then
    # organize it nicely to do various proccessing on it.
    # ... only to deliver it to a service.
    

def write_data(obj_days, obj_time):
    str_cat = "_LOG_DAYS_AND_SLOTS"
    file_o = open(str_cat, "w")
        
    for item in obj_days.text:
        file_o.writelines(item)

    file_o.writelines("\n\n")
    
    for item in obj_time.text:
        file_o.writelines(item)
        
        

driver = webdriver.Chrome(executable_path='C:/Users/garvi/Downloads/chromedriver.exe')
site_login()
redirect_scrape()

data_days_o, data_time_slots_o = retrieve_data()

