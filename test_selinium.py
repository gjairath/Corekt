# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 01:29:13 2021

@author: garvi
"""



# The BS object is being redirected to another link.
# Since Purdue uses CAS, I will have to login in to the main site and then redirect the bot
# To recwell to scrape relevant data.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class URL:
        
        #https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1
        #URL_scrape = "https://recwell.purdue.edu/"

        URL_scrape = "https://recwell.purdue.edu/Account/Login?ReturnUrl=%2Fbooking%2F83456ef4-1d99-4e58-8e66-eb049941f7c1"
        URL_login = "https://www.purdue.edu/apps/account/cas/login?service=https%3A%2F%2Fwl.mypurdue.purdue.edu"
        
        push = "5357,push"
        
        user_code = input("Enter your DUO code or just enter push: ")
        code = "5357," + str(user_code)
        
class ParsedObject:
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/garvi/Downloads/chromedriver.exe')
        self.str = "push" 
        
        self.data_days_o = ""
        self.data_time_slots_o = ""

 
    
    def site_login(self):
            
        self.driver.get (URL.URL_login)
        self.driver.find_element_by_id("username").send_keys("gjairath")
        self.driver.find_element_by_id ("password").send_keys(URL.code)
        
        submit_btn = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/form/fieldset/div[3]/div[2]/input[4]")
    
        # Once the button is found, click it.
        submit_btn.click()
        
    
    def redirect_scrape(self):
        self.driver.get(URL.URL_scrape)
        
        # wait for presence of divLoginOptions
        try:
            element_present = EC.presence_of_element_located((By.ID, "divLoginOptions"))
            WebDriverWait(self.driver, 50).until(element_present);
        except TimeoutException:
            print ("Something went wrong.")
            
        print (element_present)
        
    
        time.sleep(2)
        
        
        redirect_btn = self.driver.find_element_by_xpath(
                "/html/body/div[5]/div[4]/div/div/div/div[2]/div[2]/div[2]/div/button")        
        redirect_btn.click()
        
        try:
            user_name = self.driver.find_element_by_id("username")
        except:
            return # something weird happened purdue
        if (user_name): user_name.send_keys("gjairath")
        
        password = self.driver.find_element_by_id ("password")
        if (password): password.send_keys("5357,push")
        
        submit_btn = self.driver.find_element_by_xpath(
                        "/html/body/div[1]/div[2]/form/fieldset/div[3]/div[2]/input[4]")
        
        # Once the button is found, click it.
        if (submit_btn): submit_btn.click()
        else: return
    
        
    def retrieve_data(self):
        # flex-center margin-top-24 len is the number of available days.
        # booking-slot-item are the various "cards" that have times.
     
        data_days = self.driver.find_element_by_id("divBookingDateSelector")
        data_time_slots = self.driver.find_element_by_id("divBookingSlots")
        
        time.sleep(2)
        
        return data_days, data_time_slots
        
    # Mostly for debugging purposes.
    def write_data(self, obj_days, obj_time):
        str_cat = "_LOG_DAYS_AND_SLOTS"
        file_o = open(str_cat, "w")
            
        for item in obj_days.text:
            file_o.writelines(item)
    
        file_o.writelines("\n\n")
        
        for item in obj_time.text:
            file_o.writelines(item)
            
    
    def run(self):
        self.site_login()
        self.redirect_scrape()
        
        self.data_days_o, self.data_time_slots_o = self.retrieve_data()
        
        self.write_data(self.data_days_o, self.data_time_slots_o)
