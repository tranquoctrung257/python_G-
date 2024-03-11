# Bai13: Vòng lặp while trong python - Tự học python

# biều thức điều kiện while
# dùng khi không biết trước số lần lặp 
# cú pháp
# while điều kiện kiểm tra:
#     khôi lệnh của while

# nhập n từ bàn phím n tù 1 đến 99

n = int(input("nhập n từ bàn phím từ 1 đến 99: "))

while n < 1 or n > 99:
    n = int(input("nhập n từ bàn phím từ 1 đến 99: "))
print(n)

# while else

while n < 1 or n > 99:
    n = int("nhập n từ bàn phím từ 1 đến 99: ")
print(n)

# bài tập 
# nhập vào 
# họ tên học sinh 
# môn dự thi 
# điểm

# in ra màn hình học sinh được chọn, nếu điểm môn thi từ 7 trở lên thì đủ điều kiện lặp với học sinh khác, lặp với học sinh khác cho đến khi gõ kí tự n thì kết thúc

while True:
    hten = input("nhập tên hs: ")
    monthi = input("nhập môn thi: ")
    diem = float(input("nhập điểm: "))
    print(f"học sinh: {hten}, môn thi: {monthi}, có số điểm là {diem}")
    if diem > 7:
        print("học sinh đủ điều kiện")
    else:
        print("học sinh không đủ điều kiện")
    n = input("nhập n để thoát: ")
    if n == "N" or n == "n":
        break