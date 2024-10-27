# # Biến số nhập/xuat
# full_name = input("Nhập tên: ")
# print("Họ và tên:", full_name)

# # Biến số nguyên
# age = int(input("Nhập tuổi: "))
# print("Tuổi:", age)

# # Biến số thực
# height = float(input("Nhập chiều cao: "))
# print("Chiều cao:", height)

# if/else: câu lệnh rẽ nhánh
# num = input("Nhập vào số bất kỳ: ")
# if num % 2 == 0:
#     print("Số ", num, "là số chẵn")
# else:
#     print("Số ", num, "là số lẻ") 
# a = int(input("Nhập chiều cao bạn a: "))
# b = int(input("Nhập chiều cao bạn b: "))
# c = int(input("Nhập chiều cao bạn c: "))
# if a > b and a > c:
#     print("Chiều cao bạn a là cao nhất")
# elif b > a and b > c:
#     print("Chiều cao bạn b là cao nhất")
# else:
#     print("Chiều cao bạn c là cao nhất")

# While -> Vòng lặp vô hạn
# For -> Vòng lặp hưu hạn

# Danh sách (mảng)
# arr = ["22/08/199x", "23/08/199x", "24/08/199x"]
# arr1 = ["dog", "cat", "mouse"]

# for i in range(len(arr1)):
#     print(arr1[i])

# Hàm kiểm tra số đối xứng
def check_symmetry(num):
    return num == num[::-1]

print(check_symmetry("12321"))

# Hàm loại bỏ số trùng nhau trong mảng
def remove_duplicates(arr):
    return list(set(arr))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# Hàm tính tổng các số trong mảng
def sum_array(arr):
    return sum(arr)

print(sum_array([1, 2, 3, 4, 5]))

