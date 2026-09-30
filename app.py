import streamlit as st

st.set_page_config(
    page_title="Công Cụ Tính Lãi Gửi Tiết Kiệm",
    page_icon="🏦"
)

st.title("🏦 Công Cụ Tính Lãi Gửi Tiết Kiệm")
st.write(
    "Ứng dụng tính lãi suất tiết kiệm theo Lãi Đơn và Lãi Kép "
    "với các hình thức nhận lãi khác nhau."
)

st.divider()

# Nhập thông tin
col1, col2 = st.columns(2)

with col1:
    tien_gui = st.number_input(
        "1. Số tiền gửi (VNĐ):",
        min_value=0,
        value=100000000,
        step=1000000
    )

    ky_han = st.number_input(
        "2. Kỳ hạn gửi (tháng):",
        min_value=1,
        value=12,
        step=1
    )

with col2:
    lai_suat = st.number_input(
        "3. Lãi suất (%/năm):",
        min_value=0.0,
        value=6.5,
        step=0.1
    )

    hinh_thuc = st.selectbox(
        "4. Hình thức nhận lãi:",
        [
            "Lãnh lãi theo tháng",
            "Lãnh lãi theo quý",
            "Lãnh lãi cuối kỳ"
        ]
    )

phuong_thuc = st.radio(
    "5. Phương thức tính lãi:",
    ["Lãi Đơn", "Lãi Kép"],
    horizontal=True
)

# Tính toán
lai_suat_nam = lai_suat / 100
so_nam = ky_han / 12

if phuong_thuc == "Lãi Đơn":
    tong_lai = tien_gui * lai_suat_nam * so_nam
    tong_tien = tien_gui + tong_lai

    if hinh_thuc == "Lãnh lãi theo tháng":
        tien_lai_dinh_ky = tien_gui * lai_suat_nam / 12
    elif hinh_thuc == "Lãnh lãi theo quý":
        tien_lai_dinh_ky = tien_gui * lai_suat_nam / 4
    else:
        tien_lai_dinh_ky = tong_lai

else:
    if hinh_thuc == "Lãnh lãi theo tháng":
        so_ky = ky_han
        lai_suat_ky = lai_suat_nam / 12

    elif hinh_thuc == "Lãnh lãi theo quý":
        so_ky = ky_han / 3
        lai_suat_ky = lai_suat_nam / 4

    else:
        so_ky = 1
        lai_suat_ky = lai_suat_nam * so_nam

    tong_tien = tien_gui * (1 + lai_suat_ky) ** so_ky
    tong_lai = tong_tien - tien_gui

    if hinh_thuc == "Lãnh lãi theo tháng":
        tien_lai_dinh_ky = tien_gui * lai_suat_nam / 12

    elif hinh_thuc == "Lãnh lãi theo quý":
        tien_lai_dinh_ky = tien_gui * lai_suat_nam / 4

    else:
        tien_lai_dinh_ky = tong_lai

# Hiển thị kết quả
st.divider()

st.header("📊 Kết Quả Dự Tính")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Tiền lãi định kỳ",
        f"{tien_lai_dinh_ky:,.0f} VNĐ"
    )

with col2:
    st.metric(
        "Tổng tiền lãi thu về",
        f"{tong_lai:,.0f} VNĐ"
    )

with col3:
    st.metric(
        "Tổng gốc + lãi nhận được",
        f"{tong_tien:,.0f} VNĐ"
    )

st.write(
    f"• Tổng thời gian gửi: {ky_han} tháng "
    f"({so_nam:.1f} năm)."
)
