# class PhuongTien: # Đóng gói
#     def __init__(self, loai_xe, hang_xe, mau_sac, so_cho_ngoi, so_banh_xe, gia_tien):
#         self.loai_xe = loai_xe
#         self.hang_xe = hang_xe
#         self.mau_sac = mau_sac
#         self.so_cho_ngoi = so_cho_ngoi
#         self.so_banh_xe = so_banh_xe
#         self.gia_tien = gia_tien

#     def ThongTin(self):
#         print("Loại xe:", self.loai_xe, "\n")
#         print("Hãng xe:", self.hang_xe)
#         print("Màu sắc xe:", self.mau_sac)

# vehicle1 = PhuongTien("Xe_hoi", "Ford", "red", 7, 4, 50000000)
# vehicle1.ThongTin()

# class Pet:
#     def __init__(self, name, type, color, age, weight):
#         self.name = name
#         self.type = type
#         self.color = color
#         self.age = age
#         self.weight = weight

#     def Information(self):
#         print("Tên:", self.name)
#         print("Loại:", self.type)
#         print("Màu:", self.color)
#         print("Tuổi:", self.age)
#         print("Cân nặng:", self.weight)


# class Con:
#     pass

# dog1 = Pet("Meo", "Alaska", "Đen trắng", 3, 15)
# dog1.Information()

# meo1 = Pet("Miu", "Mèo mướp", "Tam thể", 2, 7)
# meo1.Information()



class Xe:  # Lớp cha
    def __init__(self, hang, mau_sac, gia_tien):
        self.hang = hang
        self.mau_sac = mau_sac
        self.gia_tien = gia_tien

    def khoi_dong(self):
        print("Xe", self.hang, "đang khởi động")

class XeDap(Xe): # Lớp con
    def dap_bang_hai_chan(self):
        print("Xe", self.hang, "đang được đạp về phía trước")

class XeHoi(Xe): # Lớp con
    def chay_bang_bon_banh(self):
        print("Xe", self.hang, "đang chạy về phía trước bằng động cơ")


xe_dap1 = XeDap("Martin", "Trắng", 15000)
xe_dap1.khoi_dong()
xe_dap1.dap_bang_hai_chan()