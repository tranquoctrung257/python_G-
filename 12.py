# Bai12.2: Giải bài tập python TH7 - Tự học lập trình python
# bài 7 tính năm nhuận
# năm nhuận là năm chia hết cho 400 hoặc chia hết cho 4 nhưn không chia hết cho 100

n = int(input("nhập năm: "))

if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print("n là năm nhuận")
else:
    print("n là năm ko nhuâm")


# bài 8  viểt chương trình đếm số ngày trong tháng

n = int(input("nhập tháng: "))
if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print("tháng có 31 ngày")
elif n == 4 or n == 6 or n == 9 or n == 11:
    print("tháng có 30 ngày")
elif n == 2:
    n = int(input("vui lòng nhập thêm năm: "))
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        print("n có 29 ngày")
    else:
        print("n có 28 ngày")
else:
    print("nhập sai thông tin tháng")


# bài 10
# viết chương trình kiểm tra tháng là quý mấy 
# quý 1 là tháng 1 2 3
# quý 2 4 5 6
# quý 3  7 8 9
# quý 4 10 11 12

quy = int(input("nhập vào quý: "))
if quy == 1 or quy == 2 or quy == 3:
    print("quý 1")
elif quy == 4 or quy == 5 or quy == 6:
    print("quý 2")
elif quy == 7 or quy == 8 or quy == 9:
    print("quý 3")
elif quy in (10,11,12):
    print("quý 4")
else:
    print("nhập sai tháng") 

# bài 9 viết chương trình giải phương trình bậc 2