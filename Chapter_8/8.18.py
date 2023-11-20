#Kiểm tra số hoàn hảp
#Không sử dụng function
x = int(input("Nhập số nguyên x: "))

sum_of_divisors = 0

for i in range(1, x):
    if x % i == 0:
        sum_of_divisors += i

if sum_of_divisors == x:
    print(x, "là số hoàn hảo.")
else:
    print(x, "không phải số hoàn hảo.")

#Sử dụng function
def is_perfect_number(x):
    sum_of_divisors = 0
    
    for i in range(1, x):
        if x % i == 0:
            sum_of_divisors += i
    
    if sum_of_divisors == x:
        return True
    else:
        return False

x = int(input("Nhập số nguyên x: "))

if is_perfect_number(x):
    print(x, "là số hoàn hảo.")
else:
    print(x, "không phải số hoàn hảo.")