#Tính giá trị của biểu thức
# Không sử dụng function
n = int(input("Nhập số nguyên n: "))

tong_le = 0
tong_chan = 0
tich_cac_so = 1
tich_chia_het_cho_3 = 1
tong_nguyen_to = 0
dan_dau = 0

for num in range(1, n+1):
    if num % 2 != 0:
        tong_le += num
    else:
        tong_chan += num

    tich_cac_so *= num

    if num % 3 == 0:
        tich_chia_het_cho_3 *= num

    is_prime = True
    if num >= 2:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    else:
        is_prime = False

    if is_prime:
        tong_nguyen_to += num

    dan_dau += ((-1) ** num) / (num + 1)

print("A =", tong_le)
print("B =", tong_chan)
print("C =", tich_cac_so)
print("D =", tich_chia_het_cho_3)
print("E =", tong_nguyen_to)
print("F =", dan_dau)

#Sử dụng function
#Hàm kiểm tra số nguyên tố
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#Tính toán giá trị của biểu thức
def calculate_expressions(n):
    tong_le = sum([num for num in range(1, n+1) if num % 2 != 0])
    tong_chan = sum([num for num in range(1, n+1) if num % 2 == 0])
    tich_cac_so = 1
    tich_chia_het_cho_3 = 1
    tong_nguyen_to = 0
    dan_dau= 0

    for num in range(1, n+1):
        tich_cac_so *= num
        if num % 3 == 0:
            tich_chia_het_cho_3 *= num
        if is_prime(num):
            tong_nguyen_to += num
        dan_dau += ((-1) ** num) / (num + 1)

    return tong_le, tong_chan, tich_cac_so, tich_chia_het_cho_3, tong_nguyen_to, dan_dau

n = int(input("Nhập số nguyên n: "))

A, B, C, D, E, F = calculate_expressions(n)

print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)
print("E =", E)
print("F =", F)