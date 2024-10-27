# class Cat: # Lớp(class)
#     def __init__(self, name, age, weight, type, color, sex): # method (phương thức)
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.type = type
#         self.color = color
#         self.sex = sex

# class VatNuoi: # Lớp(class)
#     def __init__(self, giong, mau_sac, tuoi, can_nang): # Phuong thức khởi tạo
#         self.giong = giong
#         self.mau_sac = mau_sac
#         self.tuoi = tuoi
#         self.can_nang = can_nang

# vat_nuoi1 = VatNuoi("Alaska", "Đen trắng", 10, 40) # Đối tượng(object)
# print("Giống:", vat_nuoi1.giong)
# print("Màu:",vat_nuoi1.mau_sac)
# print("Tuổi:",vat_nuoi1.tuoi)
# print("Can nang:",vat_nuoi1.can_nang)

# vat_nuoi2 = VatNuoi("Chiquaqua", "Vàng", 5, 10)
# print("Giống:", vat_nuoi2.giong)
# print("Màu:",vat_nuoi2.mau_sac)
# print("Tuổi:",vat_nuoi2.tuoi)
# print("Can nang:",vat_nuoi2.can_nang)



class Person:
    def __init__(self, name, age, sex, weight, height):
        self.name = name    
        self.age = age
        self.sex = sex
        self.weight = weight
        self.height = height

person1 = Person("Cao Ngọc Sơn", 2, "Nam", 63, 173)
print("Tên:", person1.name)
print("Tuổi:", person1.age)
print("Giới tính:", person1.sex)
print("Cân năng:", person1.weight)
print("Chiều cao:", person1.height)
