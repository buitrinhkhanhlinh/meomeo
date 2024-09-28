# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:34:43 2024

@author: LENOVO
"""
a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))

# Kiểm tra xem 3 cạnh có lập thành tam giác hay không
if a + b > c and a + c > b and b + c > a:
    # Kiểm tra loại tam giác
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Tam giác vuông cân")
        else:
            print("Tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Ba cạnh này không lập thành một tam giác.")