# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 03:59:03 2021

@author: garvi
"""
isTrue = True
while(isTrue):
    try:
        print (5/0)
        
        isTrue = False
    except:
        print ("s")