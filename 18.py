# Bai18: Hàm eval() tự động tính toán 1 chuỗi - python căn bản - Tự học lập trình python
a = "1+2-432*3423"
print(type(a))
print(eval(a))

# để nhập 2 số từ bàn phím cách nhau bởi dấu phẩy 
a, b = eval(input("Nhập 2 số a, b cách nhau bởi dấu phẩy: "))
print("Số thứ nhất là:", a)
print("Số thứ hai là:", b)