# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:21:37 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
km = float(input("Độ dài đoạn đường(km): "))
if km <= 1:
    Tien = km*20000
elif km <= 3:
    Tien = km*13000
elif km <= 8:
    Tien = 3*13000 + (km - 3)*12000
elif km > 8:
    Tien = 3*13000 + 5*12000 + (km - 8)*10000
if Tien > 100000:
    Tien = Tien - (Tien*0.08)
    print("Tổng tiền phải trả là:", Tien)