class sanpham:
    def __int__(self, ten_san_pham, gia, Giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__Giam_gia = Giam_gia
    def get_ten_sp(self):
        return self.__ten_san_pham
    def set_ten_sp(self, ten_sp):
        self.__ten_san_pham = ten_sp
    def get_gia_sp(self):
        return self.__gia
    def set_gia_sp(self, gia_sp):
        self.__gia = gia_sp
    def get_giam_gia(self):
        return self.__Giam_gia
    def set_giam_gia(self, giam_gia):
        self.__Giam_gia = giam_gia
    def thue_nhap_khau(self):
        return self.__gia * 0.1
    def nhap_thong_tin(self):
        self.__ten_san_pham=input(" ten san pham:")
        self.__gia=float(input("gia san pham:"))
        self.__Giam_gia=float(input("giam gia:"))
    def xuat_thong_tin(self):
        print(f"san pham:{self.__ten_san_pham},có giá:{self.__gia}được giảm giá:{self.__Giam_gia},thue_nhap_khau:{self.thue_nhap_khau()}")
    def __str__(self): 
        return f"san pham:{self.__ten_san_pham},có giá:{self.__gia}được giảm giá:{self.__Giam_gia},thue_nhap_khau:{self.thue_nhap_khau()}"


