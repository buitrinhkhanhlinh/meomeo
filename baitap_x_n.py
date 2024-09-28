# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:01:44 2024

@author: LENOVO
"""

s=0 
ts = 1
ms = 0 
n = int(input("nhap n:"))
while n <=0:
    n = int(input('nhập lại n: '))
x = float(input("nhập x: "))
for i in range (1,n+1):
    ts = x**i
    ms = ms+i
    s+= ts/ms
print(round(s,2 ))