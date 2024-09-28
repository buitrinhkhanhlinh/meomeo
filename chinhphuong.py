# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:10:43 2024

@author: LENOVO
"""

import math
n = int(input("nhập số nguyên dương n: "))
while n <= 0 :
    n =  int(input("nhập  số nguyên dương n: "))
if math.sqrt(n) == int(math.sqrt(n)):
    print ("n là số chính phương")
else: 
    print ("n không là số chính phương")