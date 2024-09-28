# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:01:33 2024

@author: LENOVO
"""

#Nhập vào số N từ bàn phím (điều kiện N nguyên dương) nếu người dùng 
#nhập không đúng thì bắt nhập lại. Sao đó in ra tất cả ước số của N.
N = int(input("Nhập một số nguyên dương: "))
while N<1: 
 N = int(input("nhập lại: "))

print(f"Các ước số của {N} là: ")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)