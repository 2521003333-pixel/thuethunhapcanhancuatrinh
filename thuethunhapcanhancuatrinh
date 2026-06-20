def tinh_thue_tncn(luong_gop, so_nguoi_phu_thuoc=0):
    # Bảo hiểm người lao động đóng
    bao_hiem = luong_gop * 0.105
    
    # Giảm trừ gia cảnh
    giam_tru_ban_than = 15500000
    giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 6200000

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        luong_gop 
        - bao_hiem 
        - giam_tru_ban_than 
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue <= 0:
        return 0

    thue = 0

    # Tính thuế lũy tiến
    bac_thue = [
        (10000000, 0.05),
        (30000000, 0.10),
        (60000000, 0.20),
        (100000000, 0.30),
        (float("inf"), 0.35)
    ]

    muc_duoi = 0

    for muc_tren, thue_suat in bac_thue:
        if thu_nhap_tinh_thue > muc_tren:
            thue += (muc_tren - muc_duoi) * thue_suat
            muc_duoi = muc_tren
        else:
            thue += (thu_nhap_tinh_thue - muc_duoi) * thue_suat
            break

    return thue


# Nhập dữ liệu
luong = float(input("Nhập lương gộp (VNĐ): "))
nguoi_phu_thuoc = int(input("Số người phụ thuộc: "))

thue = tinh_thue_tncn(luong, nguoi_phu_thuoc)

print("Thuế TNCN phải nộp:", format(thue, ",.0f"), "VNĐ")
