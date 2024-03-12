# Bai14: Vòng lặp for, continue, break - Tự học lập trình python

# for (biến lặp ) in ( đối tượng chuỗi):
#     kết cấu tần hoàn 1
# else:
    # câu lệnh 2

# for i in range(srart,stop,step):
    # code
# break continue
sum = 0
for i in range(1,6,2):
    if i == 3:
        continue
    sum = sum+i
print(sum)

# bài 11 tìm nhưng số chia hết cho 3 từ 10 đến 50

for i in range(1,51):
    if i % 3 == 0:print(i,end=" ")

print()
# bài 12 tính tỏng 1! + 2! + 3! + ... + 10!
m = 1
tong = 0
for i in range(1,11):
    m = i *m
    tong = tong + m

print(tong)

# số hoàn hảo

for i in range(1,1001):
    tong = 0
    for j in range(1,i):
        if i % j == 0:
            tong+=j
    if tong == i:
        print(i,end=" ")
    # else:
    #     print("n ko phải là số hoàn hảo")