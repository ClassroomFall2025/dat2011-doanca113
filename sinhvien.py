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

class sinhvienxldl():
  
    #các phương thức
    def __init__(self, ten_sv, nam_sinh, diem_mon, lap_trinh):
        self.Ten_Sinh_Vien = ten_sv
        self.nam_sinh = nam_sinh
        self.diem = diem_mon
        self.lap_trinh= lap_trinh

    def xuat_thong_tin(self):
        print(f"sinh viên:{self.Ten_Sinh_Vien}, sinh năm{self.nam_sinh}có điểm môn{self.diem},và học lập trình:{self.lap_trinh}")

sv1=sinhvienxldl("Đoàn Cả",2006,9,"Python")
sv1.xuat_thong_tin()

class sinhvienxldl(sinhvien):
    def __init__(self, ten_sv, nam_sinh, diem_mon, lap_trinh):
        sinhvien.__init__(self, ten_sv, nam_sinh, diem_mon)
        self.lap_trinh= lap_trinh

    def xuat_thong_tin(self):
        print(f"{sinhvien.__str__(self)} và học lập trình:{self.lap_trinh}")
    def __str__(self):
        return f"sinh viên:{self.Ten_Sinh_Vien}, sinh năm{self.nam_sinh}có điểm môn{self.diem}"
sv1=sinhvienxldl("Đoàn Cả",2006,9,"Python")
sv1.xuat_thong_tin()
