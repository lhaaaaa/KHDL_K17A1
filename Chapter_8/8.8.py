#Giá phòng
#Không sử dụng function
# In bảng giá
print("BẢNG GIÁ RESORT")
print("Mã loại\tTên loại phòng\t\tGiá 1 đêm\t\tỞ 2-3 đêm\t\tỞ từ 4 đêm")
print("--------------------------------------------------------------------------")
print("1\tStandard\t\t1,260,000\t\tGiảm 25%\t\tGiảm 30%")
print("2\tSuperior Garden View\t1,550,000")
print("3\tSuperior Ocean View\t1,830,000")
print("4\tGarden View Bungalow\t1,830,000")
print("5\tPool View Bungalow\t2,120,000")
print("6\tFamily Room\t\t2,120,000")
print("7\tBeach Front Bungalow\t2,540,000")
print("8\tVIP sea View\t\t4,800,000")
print("--------------------------------------------------------------------------")

# Nhập thông tin đặt phòng
ma_loai = int(input("Nhập mã loại phòng: "))
so_dem = int(input("Nhập số đêm thuê: "))

# Tính tiền thuê phòng
if ma_loai == 1:
    gia_1_dem = 1260000
    gia_2_3_dem = gia_1_dem * 0.75
    gia_4_dem = gia_1_dem * 0.7
elif ma_loai == 2:
    gia_1_dem = 1550000
    gia_2_3_dem = gia_1_dem
    gia_4_dem = gia_1_dem
elif ma_loai == 3:
    gia_1_dem = 1830000
    gia_2_3_dem = gia_1_dem
    gia_4_dem = gia_1_dem
elif ma_loai == 4:
    gia_1_dem = 1830000
    gia_2_3_dem = gia_1_dem
    gia_4_dem = gia_1_dem
elif ma_loai == 5:
    gia_1_dem = 2120000
    gia_2_3_dem = gia_1_dem
    gia_4_dem = gia_1_dem
elif ma_loai == 6:
    gia_1_dem = 2120000
    gia_2_3_dem = gia_1_dem
    gia_4_dem = gia_1_dem
elif ma_loai == 7:
    gia_1_dem = 2540000
    gia_2_3_dem = gia_1_dem
    gia_4_dem = gia_1_dem
elif ma_loai == 8:
    gia_1_dem = 4800000
    gia_2_3_dem = gia_1_dem
    gia_4_dem = gia_1_dem
else:
    print("Mã loại phòng không hợp lệ.")
    exit()

# Tính tổng tiền thuê phòng
if so_dem == 1:
    tong_tien = gia_1_dem
elif so_dem >= 2 and so_dem <= 3:
    tong_tien = gia_2_3_dem * so_dem
elif so_dem >= 4:
    tong_tien = gia_4_dem * so_dem
else:
    print("Số đêm thuê không hợp lệ.")
    exit()

# In kết quả
print("Tổng tiền thuê phòng là: {:.0f} VND".format(tong_tien))

#Sử dụng function
def get_room_price(ma_loai):
    if ma_loai == 1:
        return 1260000
    elif ma_loai == 2:
        return 1550000
    elif ma_loai == 3:
        return 1830000
    elif ma_loai == 4:
        return 1830000
    elif ma_loai == 5:
        return 2120000
    elif ma_loai == 6:
        return 2120000
    elif ma_loai == 7:
        return 2540000
    elif ma_loai == 8:
        return 4800000
    else:
        return None

def calculate_total_price(gia_1_dem, so_dem):
    if so_dem == 1:
        return gia_1_dem
    elif so_dem >= 2 and so_dem <= 3:
        return gia_1_dem * 0.75 * so_dem
    elif so_dem >= 4:
        return gia_1_dem * 0.7 * so_dem
    else:
        return None

# In bảng giá
print("BẢNG GIÁ RESORT")
print("Mã loại\tTên loại phòng\t\tGiá 1 đêm\t\tỞ 2-3 đêm\t\tỞ từ 4 đêm")
print("--------------------------------------------------------------------------")
print("1\tStandard\t\t1,260,000\t\tGiảm 25%\t\tGiảm 30%")
print("2\tSuperior Garden View\t1,550,000")
print("3\tSuperior Ocean View\t1,830,000")
print("4\tGarden View Bungalow\t1,830,000")
print("5\tPool View Bungalow\t2,120,000")
print("6\tFamily Room\t\t2,120,000")
print("7\tBeach Front Bungalow\t2,540,000")
print("8\tVIP sea View\t\t4,800,000")
print("--------------------------------------------------------------------------")

# Nhập thông tin đặt phòng
ma_loai = int(input("Nhập mã loại phòng: "))
so_dem = int(input("Nhập số đêm thuê: "))

# Tính tiền thuê phòng
gia_1_dem = get_room_price(ma_loai)
if gia_1_dem is None:
    print("Mã loại phòng không hợp lệ.")
    exit()

tong_tien = calculate_total_price(gia_1_dem, so_dem)
if tong_tien is None:
    print("Số đêm thuê không hợp lệ.")
    exit()

# In kết quả
print("Tổng tiền thuê phòng là: {:.0f} VND".format(tong_tien))