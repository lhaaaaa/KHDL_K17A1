#Tìm số lớn nhất (tương tự tìm số nhỏ nhất) trong 4 số
#Không dùng function
num1 = 10
num2 = 5
num3 = 20
num4 = 15

max_num = num1  # Gán giá trị đầu tiên cho max_num

if num2 > max_num:
    max_num = num2

if num3 > max_num:
    max_num = num3

if num4 > max_num:
    max_num = num4

print("Số lớn nhất là:", max_num)

#Dùng function
def find_max(a, b, c, d):
    max_num = a

    if b > max_num:
        max_num = b

    if c > max_num:
        max_num = c

    if d > max_num:
        max_num = d

    return max_num

# Test với các giá trị đầu vào
num1 = 10
num2 = 5
num3 = 20
num4 = 15

max_number = find_max(num1, num2, num3, num4)
print("Số lớn nhất là:", max_number)

# #Tìm số lớn nhất trong một dãy các số
def find_max(numbers):
    max_num = float('-inf')  # Khởi tạo số lớn nhất ban đầu với giá trị âm vô cùng

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

# Test với danh sách chứa 100 số
number_list = [17, 12, 25, 9, 36, 5, 42, 8, 19, 33, 27]  # có thể nhiều hơn

max_number = find_max(number_list)
print("Số lớn nhất là:", max_number)
