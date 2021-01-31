# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:14:40 2021

@author: garvi
"""


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

#URL_scrape = "https://recwell.purdue.edu/"
URL_scrape = "https://recwell.purdue.edu/Account/Login?ReturnUrl=%2Fbooking%2F83456ef4-1d99-4e58-8e66-eb049941f7c1"
URL_login = "https://www.purdue.edu/apps/account/cas/login?service=https%3A%2F%2Fwww.purdue.edu%2Fapps%2Fidphs%2FAuthn%2FExtCas%3Fconversation%3De1s1&entityId=https%3A%2F%2Frecwell.purdue.edu%2Fshibboleth"
#https://recwell.purdue.edu/booking/83456ef4-1d99-4e58-8e66-eb049941f7c1

def site_login():
    driver.get (URL_login)
    driver.find_element_by_id("username").send_keys("gjairath")
    driver.find_element_by_id ("password").send_keys("5357,push")
    
    submit_btn = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/form/fieldset/div[3]/div[2]/input[4]")

    # Once the button is found, click it.
    submit_btn.click()
    driver.get (URL_login)

    
    
def redirect_scrape():
    driver.get(URL_scrape)
    
    # wait for presence of divLoginOptions
    element_present = EC.presence_of_element_located((By.ID, "divLoginOptions"))
    WebDriverWait(driver, 10).until(element_present);
    


driver = webdriver.Chrome(executable_path='C:/Users/garvi/Downloads/chromedriver.exe')
site_login()


