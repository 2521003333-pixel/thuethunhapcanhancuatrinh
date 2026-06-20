            import streamlit as st

st.title("Ứng dụng tính thuế thu nhập cá nhân_NgocTrinh")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Tổng thu nhập tháng (VNĐ)",
    min_value=0,
    value=0,
    step=100000
)

bao_hiem = st.number_input(
    "Bảo hiểm bắt buộc (VNĐ)",
    min_value=0,
    value=0,
    step=100000
)

nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0,
    step=1
)

if st.button("Tính thuế"):

    # Giảm trừ gia cảnh
    giam_tru_ban_than = 15500000
    giam_tru_phu_thuoc = nguoi_phu_thuoc * 6200000

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        thu_nhap
        - bao_hiem
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue <= 0:
        thue = 0

    elif thu_nhap_tinh_thue <= 10000000:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 30000000:
        thue = (
            10000000 * 0.05
            + (thu_nhap_tinh_thue - 10000000) * 0.10
        )

    elif thu_nhap_tinh_thue <= 60000000:
        thue = (
            10000000 * 0.05
            + 20000000 * 0.10
            + (thu_nhap_tinh_thue - 30000000) * 0.20
        )

    elif thu_nhap_tinh_thue <= 100000000:
        thue = (
            10000000 * 0.05
            + 20000000 * 0.10
            + 30000000 * 0.20
            + (thu_nhap_tinh_thue - 60000000) * 0.30
        )

    else:
        thue = (
            10000000 * 0.05
            + 20000000 * 0.10
            + 30000000 * 0.20
            + 40000000 * 0.30
            + (thu_nhap_tinh_thue - 100000000) * 0.35
        )

    st.success("Kết quả tính thuế")

    st.write(
        f"Thu nhập tính thuế: {thu_nhap_tinh_thue:,.0f} VNĐ"
    )

    st.write(
        f"Thuế thu nhập cá nhân phải nộp: {thue:,.0f} VNĐ/tháng"
        )
