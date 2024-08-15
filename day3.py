# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:30:29 2024

@author:Cao Ngọc Thanh Thư 23719291
"""
GPA=float(input("Điểm trung bình GPA: "))
if GPA< 3.5:
    print("Học lực Kém")
elif 3.5<= GPA< 5.0:
    print("Học lực Yếu")
elif 5.0<= GPA< 7.0:
    print("Học lực Trung Bình")
elif 7.0<= GPA< 8.0:
    print("Học lực Khá")
elif 8.0<= GPA< 9.0:
    print("Học lực Giỏi")
else:
    print("Học lực Xuất Sắc")
