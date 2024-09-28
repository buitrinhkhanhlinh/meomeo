# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:25:40 2024

@author: LENOVO
"""

# Khởi tạo biến cho tháng và năm
month = 0
year = 0

# Sử dụng vòng lặp để yêu cầu nhập tháng và năm hợp lệ
while month < 1 or month > 12:
    month = int(input("Nhập tháng (1-12): "))
    if month < 1 or month > 12:
        print("Tháng không hợp lệ. Vui lòng nhập lại.")

year = int(input("Nhập năm: "))

# Kiểm tra năm nhuận
nhuan = False
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    nhuan = True

# Xác định số ngày trong tháng
if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31  # Tháng có 31 ngày
elif month in [4, 6, 9, 11]:
    days = 30  # Tháng có 30 ngày
elif month == 2:
    if nhuan:
        days = 29  # Tháng 2 trong năm nhuận
    else:
        days = 28  # Tháng 2 trong năm không nhuận

# In kết quả
print(f"Tháng {month} năm {year} có {days} ngày.")