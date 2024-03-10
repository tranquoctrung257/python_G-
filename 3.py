# bai 3. Biến số và các kiểu dữ liệu python - Tự học lập trình python

# 3.1 biến
a = 12
print(a)
a = 4
print(a)
a = a+1
print(a)

# để xóa a khỏi bộ nhớ 
del a
# print(a)

#3.2 các kiểu dữ liệu

# dạng dữ liệu cho số 

# 1.interger
# vd 1 2 3 -1 -2 -921
a = 1
print(type(a))

# 2.bool
# vd True False
a = True
print(type(a))
print(1==1)

# 3.Float
# vd 4.3 4.3323
a = 4.2
print(type(a))

# 4. complex( số phức )
# vd 0j 10j
a = 0j
print(type(a))

# 3.3 lệnh input và print
# để nhập từ bàn phím dùng hàm input()
# để xuất ra màn hình dùng hàm print()
# để kiểm tra kiểu dữ liệu dùng hàm type()
# mặc định của input là str

bien = input("nhập vào giá trị từ bàn phím: ")
print(bien)

# ví dụ
a = int(input("nhập a từ bàn phím: "))
print(a+5)
print(type(a))

# 3.4 chú thích trong python 
# dùng dấu #
# hoặc dùng chú thích trong nhiều dòng
"""
python
c++
c#
"""