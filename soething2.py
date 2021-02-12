# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 00:01:06 2021

@author: garvi
"""


import sys

# These snippets are inspired by geek for geeks 
# Credit to MITS, GeekforGeeks.

def divide(dividend, divisor):
     
     
    sign = (-1 if((dividend < 0) ^ 
                  (divisor < 0)) else 1);
     

    dividend = abs(dividend);
    divisor = abs(divisor);
     
    quotient = 0;
    temp = 0;
     
    # test down from the highest 
    # bit and accumulate the 
    # tentative value for valid bit
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i;
            quotient |= 1 << i;
     
    return sign * quotient;


def m(n, m): 
    
    if (m < 0 and n >= 0):
        temp = n
        n = m
        m = temp
    
    sign = 0
    if (n < 0 and m < 0):
        sign = 1
    ans = 0
    count = 0
    while (m): 


        if (m % 2 == 1): 
            ans += n << count 
  

        count += 1
        m = int(m/2) 
  
    if (sign == 1):
        ans = -1 * ans
    return ans 

   

# A multiplicative inverse is st ax = 1, eg, 4 % 11, x = 3.

def BIMI(num,mod):
    NUM = num; MOD = mod
    x, x_old = 0, 1
    y, y_old = 1, 0


    while mod:
        q = divide(num, mod)

#        q = num // mod
        num, mod = mod, num % mod
        x, x_old = x_old - m(q,x), x
        y, y_old = y_old - m(q,y), y
    if num != 1:
        return 0
    else:
        MI = (x_old + MOD) % MOD
        return MI


#x=BIMI(15, 4)
    #31, 73714876143    = 45180085378
    #19, 1212393831     = 701912218
    #3, 73714876143     = NI.
    #7, 87              = 25
    #465135354 354318437468743  = 202759811091371
    #76435, 4                   = 3

    #what a sexy testing lols. xD
y = BIMI(76435,4)
print (y)
