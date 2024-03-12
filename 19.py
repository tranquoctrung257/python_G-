# Bai19: Hàm lấy số ngẫu nhiên - random python - Tự học lập trình python

import random

# in ra số sandom từ 1 đến 100
a = random.randrange(1,10)
b = random.randrange(101)
print(a)
print(b)

c = 3
while a != c:
    c = int(input("nhập lại: "))
    print(a)
print(("bạn nhập chính sác"))

