import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính Lãi Gửi Tiết Kiệm",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰 CÔNG CỤ TÍNH LÃI GỬI TIẾT KIỆM")

st.write(
    "Ứng dụng tính tiền lãi tiền gửi theo phương pháp "
    "lãi đơn và lãi kép."
)

st.divider()

# =========================
# NHẬP THÔNG TIN
# =========================

st.subheader("📌 Thông tin tiền gửi")

col1, col2 = st.columns(2)

with col1:
    tien_gui = st.number_input(
        "💵 Số tiền gửi (VNĐ)",
        min_value=0,
        value=10000000,
        step=1000000,
        format="%d"
    )

    ky_han = st.number_input(
        "📅 Kỳ hạn (tháng)",
        min_value=1,
        value=12,
        step=1
    )

with col2:
    lai_suat = st.number_input(
        "📈 Lãi suất (%/năm)",
        min_value=0.0,
        value=6.0,
        step=0.1,
        format="%.2f"
    )

    phuong_phap = st.selectbox(
        "🧮 Phương pháp tính lãi",
        ["Lãi đơn", "Lãi kép"]
    )

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Lãnh lãi theo tháng",
        "Lãnh lãi theo quý",
        "Lãnh lãi cuối kỳ"
    ]
)

st.divider()

# =========================
# NÚT TÍNH
# =========================

if st.button("🧮 TÍNH TIỀN LÃI", use_container_width=True):

    # Chuyển lãi suất từ % sang số thập phân
    r = lai_suat / 100

    # Số năm gửi
    so_nam = ky_han / 12

    # =========================
    # LÃI ĐƠN
    # =========================
    if phuong_phap == "Lãi đơn":

        tong_lai = tien_gui * r * so_nam

        tong_tien = tien_gui + tong_lai

        # Lãi định kỳ
        if hinh_thuc == "Lãnh lãi theo tháng":
            lai_dinh_ky = tien_gui * r / 12
            don_vi = "tháng"

        elif hinh_thuc == "Lãnh lãi theo quý":
            lai_dinh_ky = tien_gui * r / 4
            don_vi = "quý"

        else:
            lai_dinh_ky = tong_lai
            don_vi = "cuối kỳ"

    # =========================
    # LÃI KÉP
    # =========================
    else:

        # Lãnh lãi theo tháng
        if hinh_thuc == "Lãnh lãi theo tháng":

            so_ky = ky_han
            lai_ky = r / 12

            tong_tien = tien_gui * (1 + lai_ky) ** so_ky
            tong_lai = tong_tien - tien_gui

            # Lãi của kỳ đầu tiên
            lai_dinh_ky = tien_gui * lai_ky
            don_vi = "tháng"

        # Lãnh lãi theo quý
        elif hinh_thuc == "Lãnh lãi theo quý":

            so_ky = ky_han / 3
            lai_ky = r / 4

            tong_tien = tien_gui * (1 + lai_ky) ** so_ky
            tong_lai = tong_tien - tien_gui

            # Lãi của quý đầu tiên
            lai_dinh_ky = tien_gui * lai_ky
            don_vi = "quý"

        # Lãnh lãi cuối kỳ
        else:

            tong_tien = tien_gui * (1 + r) ** so_nam
            tong_lai = tong_tien - tien_gui

            lai_dinh_ky = tong_lai
            don_vi = "cuối kỳ"

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.success("✅ Đã tính toán thành công!")

    st.subheader("📊 KẾT QUẢ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💵 Lãi định kỳ",
            f"{lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "📈 Tổng tiền lãi",
            f"{tong_lai:,.0f} VNĐ"
        )

    with col3:
        st.metric(
            "💰 Tổng gốc + lãi",
            f"{tong_tien:,.0f} VNĐ"
        )

    st.divider()

    # =========================
    # THÔNG TIN TÓM TẮT
    # =========================

    st.subheader("📋 Thông tin khoản gửi")

    st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Phương pháp:** {phuong_phap}")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

    if hinh_thuc != "Lãnh lãi cuối kỳ":
        st.info(
            f"💡 Tiền lãi định kỳ ({don_vi}): "
            f"{lai_dinh_ky:,.0f} VNĐ"
        )

    st.caption(
        "Lưu ý: Kết quả mang tính mô phỏng theo công thức toán học, "
        "chưa xét các quy định riêng của từng ngân hàng."
    )
