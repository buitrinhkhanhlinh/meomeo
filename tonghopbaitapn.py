# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:14:44 2024

@author: LENOVO
"""
#1+2+3+...+n
n = int(input("Nhập n (n > 0): "))
S = 0
for i in range(1, n + 1):
    S += i
print("Tổng S =", S)

#1^2+2^2+3^2+...n^2
n = int(input("Nhập n (n > 0): "))
S = 0
for i in range(1, n + 1):
    S += i ** 2
print("Tổng S =", S)

#n chẵn
n = int(input("Nhập n (n chẵn > 0): "))
S = 0
for i in range(2, n + 1, 2):
    S += i
print("Tổng S =", S)

#n lẻ
n = int(input("Nhập n (n lẻ > 0): "))
S = 1
for i in range(1, n + 1):
    S *= i
print("Giai thừa S =", S)

# 1/n
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += 1/i
print(f"Kết quả Bài 39: {S}")

#1/2n 
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += 1/(2*i)
print(f"Kết quả Bài 40: {S}")

#1/n l
n = int(input("Nhập n: "))
S = 0
for i in range(n+1):
    S += 1/(2*i+1)
print(f"Kết quả Bài 41: {S}")

#1/(n(n+1)
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += 1/(i*(i+1))
print(f"Kết quả Bài 42: {S}")

#n/(n+1)
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += i/(i+1)
print(f"Kết quả Bài 43: {S}")

#có x và n
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = x
for i in range(2, n+1):
    denominator = sum(range(1, i+1))
    S += x**i / denominator
print(f"Kết quả Bài 45: {S}")

# 2n+1 / 2n +2
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += (2*i+1) / (2*i+2)
print(f"Kết quả Bài 44: {S}")

