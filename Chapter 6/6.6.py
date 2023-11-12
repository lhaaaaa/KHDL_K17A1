#Nhập số kẹo của Alice
alice_candies = int(input("Alice's candies: \n"))

#Nhập số kẹo của Bob
bob_candies = int(input("Bob's candies: \n"))

#Nhập số kẹo của Carol
carol_candies = int(input("Carol's candies: \n"))

#Tính tổng số kẹo của 3 bạn
sum_candies = alice_candies + bob_candies + carol_candies

#Tính số kẹo còn dư sau khi chia đêu cho 3 bạn
to_smash = sum_candies % 3

#In ra màn hình kết quả
print("Số kẹo còn lại sau khi chia đều cho 3 bạn là:", to_smash, "cái")