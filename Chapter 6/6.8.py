#Nhập vào từ bàn phím chuỗi s1
s1 = input("Chuỗi s1: \n")

#Nhập vào từ bàn phím chuỗi s2
s2 = input("Chuỗi s2: \n")

#Nhập vào từ bàn phím chuỗi s3
s3 = input("Chuỗi s3: \n")

#Nhập index
index = int(input("Nhập index: \n"))

#Để biết được chiều dài của chuỗi, ta sử dụng hàm len()
print("Chiều dài của chuỗi s1 là:", len(s1))
print("Chiều dài của chuỗi s2 là:", len(s2))

#Tạo chuỗi con s4 từ chuỗi s1 với nội dung từ index đến hết chuỗi
#Để lấy nội dung từ một index, ta sử dụng chuỗi[index:]
s4 = s1[index:]
print("Chuỗi s4 được tạo ra là:", s4)

#Để lặp lại chuỗi, ta sử dụng toán tử *
print("Chuỗi s2 sau khi được lặp lại", index, "lần là:", s2*index)