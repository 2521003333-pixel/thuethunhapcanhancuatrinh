import streamlit as st
st.image("IMG_20260425_142016.jpg")


st.title("Ứng dụng tính Thuế Thu nhập cá nhân của Ngọc Trinh")

# Nhập dữ liệu
luong = st.number_input(
    "Nhập lương gộp hàng tháng (triệu đồng)",
    min_value=0.0,
    value=20.0
)

nguoi_phu_thuoc = st.number_input(
    "Nhập số người phụ thuộc",
    min_value=0,
    value=0
)

if st.button("Tính thuế"):

    # Tính bảo hiểm người lao động phải đóng
    bao_hiem = luong * 0.105

    # Tính giảm trừ gia cảnh
    giam_tru_ban_than = 15.5
    giam_tru_phu_thuoc = nguoi_phu_thuoc * 6.2

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        luong
        - bao_hiem
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    # Tính thuế lũy tiến từng phần
    if thu_nhap_tinh_thue <= 0:
        thue = 0

    elif thu_nhap_tinh_thue <= 10:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 30:
        thue = (
            10 * 0.05
            + (thu_nhap_tinh_thue - 10) * 0.10
        )

    elif thu_nhap_tinh_thue <= 60:
        thue = (
            10 * 0.05
            + 20 * 0.10
            + (thu_nhap_tinh_thue - 30) * 0.20
        )

    elif thu_nhap_tinh_thue <= 100:
        thue = (
            10 * 0.05
            + 20 * 0.10
            + 30 * 0.20
            + (thu_nhap_tinh_thue - 60) * 0.30
        )

    else:
        thue = (
            10 * 0.05
            + 20 * 0.10
            + 30 * 0.20
            + 40 * 0.30
            + (thu_nhap_tinh_thue - 100) * 0.35
        )

    # Hiển thị kết quả
    st.success("Kết quả tính thuế")

    st.write(
        f"📌 Bảo hiểm phải đóng: {bao_hiem:.2f} triệu đồng"
    )

    st.write(
        f"📌 Thu nhập tính thuế: {max(thu_nhap_tinh_thue, 0):.2f} triệu đồng"
    )

    st.write(
        f"📌 Thuế thu nhập cá nhân phải nộp: {thue:.2f} triệu đồng/tháng"
        )
