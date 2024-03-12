# Bai15: Vòng lặp for lồng nhau, ứng dụng vẽ chữ N, hình trái tim - Tự học lập trình python

# bài 1 xuất bảng cửu chương

n = 3
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i * j}" )
    print()

# vẽ chữ N
n = 5
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i ==j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i+j == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()