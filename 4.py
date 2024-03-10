# bai4: Kiểu string các công thức cơ bản Python -Tự học lập trình python

# string sử dụng "", '',''' ''',""" """
# + để nối
# * để copy string

a = "xin chào"
print(type(a))

b = """
chúc mừng năm mới
"""
print(b)
print(type(b))

chuoi = a + b
print(chuoi)

print(chuoi * 5)
print("-" * 5)

# các phép tính toán thông thường
# phép cộng +
# phép trừ -
# phép nhân * 
# phép chia /
# phép chia lấy phần nguyên //
# phép chia lấy phần dư % 
# lũy thừa mũ **

# cấc phép so sánh 
# == bằng nhau
# != khác bằng
# > lớn hơn
# < bé hơn 
# >= lớn hơn hoặc bằng
# <= bé hơn hoặc bằng

# các phép tính tích hợp
# += gán cộng x+=y ==> x = x + y
# -= gán cộng x-=y ==> x = x = y
# *= gán cộng x*=y ==> x = x * y
# /= gán cộng x/=y ==> x = x / y
# //= gán cộng x//=y ==> x = x // y
# **= gán cộng x**=y ==> x = x ** y
# %= gán cộng x%=y ==> x = x % y

# bài tập 

# bài 1
a = 10
b = 203
print(b % a)

# bài 2 viết chương trình nhập vào từ bàn phím bán kính r cùa đường tròn, in ra kết quả ( cho pi = 3.14)
# a chu vi
# b dien tich
# gợi ý:
# chu vi = 2 * r * 3.14
# dientich = 3.14 * r^2

import math

r = float(input("nhập r từ bàn phím: "))
print("Chu vi: ",2 * r * math.pi )
print(f"Diện tích: {math.pi * r **2 }")
print("Diện tích: {} ".format(math.pi * r **2 ))