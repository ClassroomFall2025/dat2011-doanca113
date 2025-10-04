class sinhvien:
    #các thuộc tính
    Ten_Sinh_Vien = ""
    nam_sinh= ""
    diem= ""
    #các phương thức
    def them_sinh_vien(self, ten_sv, nam_sinh, diem_mon):
        self.Ten_Sinh_Vien = ten_sv
        self.nam_sinh = nam_sinh
        self.diem = diem_mon
    def xuat_thong_tin(self):
        print(f"sinh viên:{self.Ten_Sinh_Vien}, sinh năm{self.nam_sinh}có điểm môn{self.diem}")

sv1=sinhvien()
sv1.them_sinh_vien("Đoàn Cả", 2006, 9)
sv1.xuat_thong_tin()
