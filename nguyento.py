# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:43:53 2024

@author: LENOVO
"""

n = int(input("nhập số nguyên dương n: "))
while n < 0:
    n = int(input("nhập lại số nguyên dương n: "))
if n < 2:
    print ("n không phải là số nguyên tố")
else:
    for i in range (2, n+1 ):
        if n%i == 0:
            print ("không là số nguyên tố")
            break 
        else:
            print ("n là số nguyên tố")
            break 
        
        
    