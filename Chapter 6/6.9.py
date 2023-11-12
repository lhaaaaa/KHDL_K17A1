#Nhập vào lãi suất 1 năm
lai_suat = float(input("Nhập vào lãi suất 1 năm (%): \n"))

#Nhập vào số tiền gửi
so_tien_gui = int(input("Nhập vào số tiền gửi: \n"))

#Nhập vào kỳ hạn gửi
ky_han = int(input("Nhập vào kỳ hạn gửi (tháng): \n"))

#Tính số tiền lãi
tien_lai = int((so_tien_gui * ky_han) * ((lai_suat/100)/12))

#Tính số tiền nhận được
so_tien_nhan_duoc = int(so_tien_gui + tien_lai)

#In ra màn hình kết quả
print("Số tiền lãi nhận được là:", tien_lai)
print("Số tiền cả gốc lẫn lãi là:", so_tien_nhan_duoc)