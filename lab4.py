def Tinh_Tien_Nuoc(sonuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if sonuoc <= 10:
        tien_nuoc_thang= sonuoc * gia_ban_nuoc[0]
    elif sonuoc <= 20:
        tien_nuoc_thang=10*gia_ban_nuoc[0]*(sonuoc-10)+gia_ban_nuoc[1]
    elif sonuoc <= 30:
        tien_nuoc_thang=10*gia_ban_nuoc[0]*10*gia_ban_nuoc[1]+(sonuoc-20)*gia_ban_nuoc[2]
    else:
        tien_nuoc_thang=10*gia_ban_nuoc[0]*10*gia_ban_nuoc[1]*10*gia_ban_nuoc[2]+(sonuoc-30)*gia_ban_nuoc[3]
    return tien_nuoc_thang


def tinh_nguyen_lieu(dauxanh, thapcam, banhdeo):
    dauxanh = {"duong": 0.04,"dau": 0.07}
    thapcam = {"duong": 0.06,"dau": 0}
    banhdeo = {"duong": 0.05,"dau": 0.02}
    duong_lam_banh= dauxanh["duong"] * 0.04 + thapcam["duong"] * 0.06 + banhdeo["duong"] * 0.05
    dau_lam_banh= dauxanh["dau"] * 0.07 + thapcam["dau"] * 0 + banhdeo["dau"] * 0.02
    tinh_nguyen_lieu["duong"]= duong_lam_banh
    tinh_nguyen_lieu["dau"]= dau_lam_banh
    return tinh_nguyen_lieu

