#Tính và in ra diện tích tam giác
#Không sử dụng function
import math

# Nhập độ dài ba cạnh từ bàn phím
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

# Kiểm tra tính hợp lệ của tam giác
if a + b > c and b + c > a and a + c > b:
    # Tính nửa chu vi
    p = (a + b + c) / 2

    # Tính diện tích tam giác bằng công thức Heron
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    # In kết quả
    print("Diện tích tam giác là:", area)
else:
    print("Ba cạnh không tạo thành một tam giác hợp lệ.")

#Sử dụng function
import math

def calculate_triangle_area(a, b, c):
    # Tính nửa chu vi
    half_perimeter = (a + b + c) / 2

    # Tính diện tích tam giác bằng công thức Heron
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return area

def is_valid_triangle(a, b, c):
    # Kiểm tra tính hợp lệ của tam giác
    return a + b > c and b + c > a and a + c > b

# Nhập độ dài ba cạnh từ bàn phím
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

# Kiểm tra tính hợp lệ của tam giác
if is_valid_triangle(a, b, c):
    # Tính diện tích tam giác
    triangle_area = calculate_triangle_area(a, b, c)

    # In kết quả
    print("Diện tích tam giác là:", triangle_area)
else:
    print("Ba cạnh không tạo thành một tam giác hợp lệ.")