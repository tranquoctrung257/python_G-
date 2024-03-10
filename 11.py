# Bai11: Bài tập python Câu lệnh if elif else - Tự học lập trình python

# bài 5 viết chương trình nhập vào 1 số nguyên từ bàn phím in ra kết quả là chẵn hay lẻ

n = int(input("nhập n từ bàn phím: "))
print("chẵn" if n % 2 == 0 else "lẻ") 

# bài 6 viết chương trình nhập vào điểm trung bình mon cho biết điểm đó thuộc khá giỏi trung bình yếu
# >= 9.0 loại giỏi
# từ 7 đén < 9.0 loại khá
# từ 5.0 đến < 7.0 loại trung bình
# < 5.0 yếu

diem = float(input("nhập điểm từ bàn phím: "))
if diem >= 9.0:
    print("giỏi")
elif diem >= 7.0 and diem < 9.0:
    print("khá")
elif diem >= 5.0 and diem < 7.0:
    print("trung bình")
elif diem >= 0 and diem < 5.0:
# hoặc 
# elif 5<=dtb>0
    print("yếu")
else:
    print("nhập sai")