#BCNN
#Không sử dụng function
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

max_num = a if a > b else b

while True:
    if max_num % a == 0 and max_num % b == 0:
        bcnn = max_num
        break
    max_num += 1

print("Bội chung nhỏ nhất của a và b là:", bcnn)

#Sử dụng function
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

bcnn = find_lcm(a, b)

print("Bội chung nhỏ nhất của a và b là:", bcnn)