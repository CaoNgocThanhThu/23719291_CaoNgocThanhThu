# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:25:12 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a= float(input("Nhập a(a<>0): "))
b= float(input("Nhập b: "))
c= float(input("Nhập c: "))
delta=b**2-4*a*c
if delta <0:
    print("Phương trình VÔ NGHIỆM")
if delta >0:
    print("Phương trình có HAI NGHIỆM PHÂN BIỆT x1=",(-b + delta**0.5)/2*a, "and x2=",(-b - delta**0.5)/2*a)
if delta ==0:
    print("Phương trình có NGHIỆM KÉP x1=x2",-b/2*a)