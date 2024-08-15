# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:19:10 2024

@author: Cao Ngọc Thanh Thư 23719291
"""

import math
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
def kiem_tra_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def phan_loai_tam_giac(a, b, c):
    if not kiem_tra_tam_giac(a, b, c):
        return "a, b, c KHÔNG PHẢI cạnh của tam giác"
    
    if a == b == c:
        return "Tam Giác Đều"
    elif a == b or a == c or b == c:
        if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            return "Tam Giác Vuông Cân"
        else:
            return "Tam Giác Cân"
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return "Tam Giác Vuông"
    else:
        return "Tam Giác Thường"
loai_tam_giac = phan_loai_tam_giac(a, b, c)
print(loai_tam_giac)
