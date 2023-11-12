#Nhập vào từ bàn phím nhiệt độ theo đơn vị độ C
celsius = float(input("Nhiệt độ theo độ C là: \n"))

#Đổi đơn vị từ độ C sang đô F
fahrenheit = 9/5 * celsius + 32

#In ra màn hình kết quả
print("Đổi nhiệt độ từ", celsius, "độ C sang độ F được", fahrenheit, "độ F")