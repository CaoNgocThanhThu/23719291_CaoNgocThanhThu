# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:53:39 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a= float(input("Nhập độ dài cạnh a: "))
b= float(input("Nhập độ dài cạnh b: "))
c= float(input("Nhập độ dài cạnh c: "))
if a + b > c or a + c > a or c + a > b:
    print("a,b,c là 3 cạnh của tam giác")
else:
    print("a,b,c KHÔNG PHẢI là cạnh của tam giác")