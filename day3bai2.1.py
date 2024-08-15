# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:11:03 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a= float(input("Nhập a: "))
b= float(input("Nhập b: "))
if a== 0 and b != 0:
    print("Phương trình VÔ NGHIỆM")
elif a==0 and b== 0:
    print("Phương trình có VÔ SỐ NGHIỆM")
else:
    print("Nghiệm của phương trình là:", -b/a)