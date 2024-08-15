# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:03:59 2024

@author: Cao Ngọc Thanh Thư 23719291
"""

import random
luachon = ('KÉO', 'BÚA', 'BAO')
nguoichoi = input("LỰA CHỌN (KÉO, BÚA, BAO)")
may = random.choice(luachon)
print(f"Bạn chọn: {nguoichoi}")
print(f"Máy chọn: {may}")
if nguoichoi == may:
    print("HÒA")
elif may == "BÚA" and nguoichoi == "KÉO" or\
     may == "KÉO" and nguoichoi == "BAO" or\
     may == "BAO" and nguoichoi == "BÚA":
         print("MÁY THẮNG")
else:
    print("MÁY THUA")