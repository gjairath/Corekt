# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 01:38:55 2021

@author: garvi

Filename: process_data.py
"""

import test_selinium as ts
import sys


class ProcessData():
    
    def __init__(self):
        self.parsed = ts.ParsedObject()
        self.parsed.run()
        
        #raw array needs to be processed
        #shows first day by default
        try:
            string = self.parsed.data_days_o.text
            string = string[string.find("2021") + 5: ]
            self.days = string.split("\n")
        except:
            print ("The programmer has made a stupid mistake, contact him to fix it. [It's an easy fix]")
            exit()
        
      #  self.days = self.parsed.data_days_o.text.split("2021\n")[1].split("\n")
        self.time_slots = self.parsed.data_time_slots_o.text.split("BOOK NOW\n")

    
    
    def refetch_data_time(self):
        _, time_slots = self.parsed.retrieve_data()
        string = time_slots.text.replace("UNAVAILABLE", "BOOK NOW")
        self.time_slots = string.split("BOOK NOW\n")


    
    def show_days(self):

        
        for item in self.days:
            if (item.isnumeric()):
                self.days.remove(item)
                
        print ("\n\n---DAYS-----\n")
        
        for item in self.days:
            print (item, end = ", ")
            
        return self.days
    
    def processing_data(self):
        

        print ("\n\n----------\n\n")
        isBooked = False
        if (len(self.time_slots) == 1):
            self.time_slots = self.time_slots[0].split("UNAVAILABLE")
            isBooked = True
            
        self.time_slots.pop(0)


        for idx, item in enumerate(self.time_slots):                
            self.time_slots[idx] = item.split("\n")
        
        if (isBooked == True):            
            for item in (self.time_slots):
                    del item[0]
                    if(len(item) > 2): del item[2]

                

            
        for item in self.time_slots:
            if (len(item) == 3): del item[2]
                            
        
        return self.time_slots, isBooked
        
    
    def reset(self):
        self.days = self.parsed.data_days_o.text.split("2021\n")[1].split("\n")
        string = self.parsed.data_time_slots_o.text
        string = string.replace("UNAVAILABLE", "BOOK NOW")
        
        self.time_slots = string.split("BOOK NOW\n")
    
    