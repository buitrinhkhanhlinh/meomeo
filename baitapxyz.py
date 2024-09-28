# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:31:52 2024

@author: LENOVO
"""
#bài tìm tập 
ds = []
for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                ds += [(x,y,z)]
if ds:
    print (f'{ds}')

#tìm nghiệm lớn nhất
lon_nhat = 0
bo_nhiem = 0
for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                tong = x+y+z
                if tong > lon_nhat:
                    lon_nhat = tong
                    bo_nghiem = (x,y,)
                
if bo_nghiem:
    print (f'{bo_nghiem} voi {x,y,z} = {lon_nhat}')
    
#tìm nghiệm lớn nhất
_nhat = 989
bo_nhiem = 0
for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                tong = x+y+z
                if tong < _nhat:
                    _nhat = tong
                    bo_nghiem = (x,y,)
                
if bo_nghiem:
    print (f'{bo_nghiem} voi {x,y,z} = {_nhat}')