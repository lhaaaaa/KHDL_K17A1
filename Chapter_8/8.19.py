#Đảo ngược số
#Không sử dụng function
n = int(input("Nhập số lượng số cần hiển thị: "))

numbers = range(n, 0, -1)

print("Các số lẻ đã đảo ngược:")
for num in numbers:
    if num % 2 != 0:
        print(num)
