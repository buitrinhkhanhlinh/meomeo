# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:40:16 2024

@author: LENOVO
"""
km = float(input("nhập số km: "))
# Tính tiền cước
if km <= 1:
    tien_cuoc = 15000
elif km <= 5:
    tien_cuoc = 15000 + (km - 1) * 13500
elif km <= 120:
    tien_cuoc = 15000 + 4 * 13500 + (km - 5) * 11000
else:
    tien_cuoc = 15000 + 4 * 13500 + (120 - 5) * 11000 + (km - 120) * 11000
    tien_cuoc *= 0.9  # Giảm 10%

# In ra tổng tiền cước
print(f"Tổng tiền cước taxi là: {tien_cuoc:.0f} VND")