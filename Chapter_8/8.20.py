#Tính e^x
# Không sử dụng function
import math

# Nhập giá trị x và số lượng các mục trong chuỗi từ bàn phím
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số lượng các mục trong chuỗi (n): "))

exponential_value = 1
factorial = 1

for i in range(1, n+1):
    factorial *= i
    exponential_value += (x ** i) / factorial

# In ra kết quả
print(f"Giá trị của e^{int(x)} là: {exponential_value}")

#Sử dụng function
import math

def calculate_exponential_recursive(x, n):
    if n == 0:
        return 1
    else:
        return calculate_exponential_recursive(x, n-1) + (x**n) / math.factorial(n)

# Nhập giá trị x và số lượng các mục trong chuỗi từ bàn phím
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số lượng các mục trong chuỗi (n): "))

# Tính giá trị của e^x bằng cách sử dụng công thức truy hồi
exponential_value = calculate_exponential_recursive(x, n)

# In ra kết quả
print(f"Giá trị của e^{int(x)} là: {exponential_value}")