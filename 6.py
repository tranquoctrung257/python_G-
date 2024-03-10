# bai6: Giải bài tập python TH3 tính trung bình cộng - Tự học lập trình python

# bài 3 viết chương trình 
# 1 . nhập vào bàn phím thời gian chạy của 3 vận động viên
# 2. xuất ra màn hình thời gian trung bình của 3 vận động viên

a = float(input("nhập thời gian chạy của vận động viên thứ nhất: "))
b = float(input("nhập thời gian chạy của vận động viên thứ hai: "))
c = float(input("nhập thời gian chạy của vận động viên thứ ba: "))

tb = (a + b + c ) / 3
# để làm tròn thì dùng hàm round(số,cần làm tròn bao nhiêu dấu ,)
print("thời gian trung bình của 3 vận động viên là {}".format(round(tb,2)))