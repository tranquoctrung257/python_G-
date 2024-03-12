import time

giay = time.time()
# trả về số giây tính từ 0:0:00 1/1/1970
hientai = time.ctime(giay)
print(hientai)


print("nhập đáp án:")
# time.sleep(4)
print("hết giờ")

# trả về năm hiện tại tháng tuần theo giờ địa phương

"""
Chỉ số	Thuộc tính	Mô tả
0	tm_year	Năm hiện tại: 0000, ...., 2018, ..., 9999
1	tm_mon	Tháng hiện tại: 1, 2, ..., 12
2	tm_mday	Ngày hiện tại: 1, 2, ..., 31
3	tm_hour	Giờ hiện tại: 0, 1, ..., 23
4	tm_min	Phút hiện tại: 0, 1, ..., 59
5	tm_sec	Giây hiện tại: 0, 1, ..., 61
6	tm_wday	Ngày trong tuần: 0, 1, ..., 6; Monday tính là 0
7	tm_yday	Ngày trong năm: 1, 2, ..., 366
8	tm_isdst	Xác định DST: 0, 1 hoặc -1
"""
tg = time.localtime()
print(tg)
print("năm hiện tại",tg.tm_year)

# trả về ngày h phút giây hiện tại theo dạng str 
"""
Ở ví dụ này, %Y, %m, %d, %H là các code định dạng.

%Y: năm [0001,..., 2018, 2019,..., 9999]
%m: tháng [01, 02, ..., 11, 12]
%d: ngày [01, 02, ..., 30, 31]
%H: giờ [00, 01, ..., 22, 23
%M: tháng [00, 01, ..., 58, 59]
%S: giây [00, 01, ..., 58, 61]
"""
t = time.strftime("%Y:%m:%d| %H:%M:%S")
print(type(t))
print(t)

# bài tập ví dụ nhập tuổi của bạn đếm xem bao nhiêu năm nữa bạn sẽ 100 tuổi

tuoi = 34
hientai = time.localtime()
nam = hientai.tm_year
print(nam)
print(f"năm bạn đạt 100 tuổi là {(100-tuoi)+nam} " )