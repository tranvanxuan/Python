class SieuNhan:
    suc_manh=50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten=para_ten
        self.vu_khi=para_vu_khi
        self.mau_sac=para_mau_sac
        
class SieuNhanKteam(SieuNhan):
    suc_manh=40
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_so_thu):
        super().__init__(para_ten, para_vu_khi, para_mau_sac)
        self.su_thu = para_so_thu

gao_do = SieuNhanKteam("Gao do", "Cung", "Do", "Su tu")
print(gao_do.__dict__)
print(gao_do.suc_manh)



# class SieuNhanGao(SieuNhan):
#     suc_manh = 40
#     def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_su_thu):
#         super().__init__(para_ten, para_vu_khi, para_mau_sac)
#         self.su_thu = para_su_thu

# gao_do = SieuNhanGao("Gao do", "Cung", "Do", "Su tu")
# print(gao_do.__dict__)
# print(gao_do.suc_manh)