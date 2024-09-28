# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:19:32 2024

@author: LENOVO
"""

#. Tính tổng các chữ số N nguyên dương. (Nhập N = 6789 thì 6+7+8+9 = 30)
tong = 0
N = int(input("Nhập một số nguyên dương: "))
while N<0:
 N = int(input("nhập lại: "))
for digit in str(N):
    tong += int(digit)

print(f"Tổng các chữ số của {N} là: {tong}")