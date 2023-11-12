#Nhập vào từ bàn phím số lượng
so_luong = int(input("Số lượng: \n"))
#Nhập vào từ bàn phím đơn giá
don_gia = int(input("Đơn giá: \n"))
#Tính giá trị đơn hàng
thanh_tien = so_luong * don_gia
#In ra màn hình kết quả
print("Thành tiền:", so_luong, "*", don_gia, "=", thanh_tien)