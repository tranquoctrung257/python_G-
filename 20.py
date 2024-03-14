# Bai20: Giải thích chi tiết hàm define python def python - Tự học lập trình python

# trong python có 2 lại hàm 
# 1 hàm thư viện
# 2 hàm tự định nghĩa

# def name(list tham số):
#     khối lệnh

def cong(x,y):
    return x,y

# hàm có đối số
def tru(x,y):
    return x-y

# hàm không có tham số
def nhan(x,y):
    print(x*y)

def n():
    n = 10
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n -1 or j + i == n -1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
n()