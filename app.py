import streamlit as st
from users import users
from tax_data import tax_records

st.set_page_config(page_title="Tra cứu Thuế", page_icon="🔍", layout="centered")

st.markdown("## 🔒 Đăng nhập hệ thống tra cứu thuế")

# Khởi tạo trạng thái đăng nhập nếu chưa có
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# Nếu chưa đăng nhập, hiển thị form đăng nhập
if not st.session_state.logged_in:
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")

    if st.button("Đăng nhập"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("✅ Đăng nhập thành công!")
            st.experimental_rerun()  # Tải lại để chuyển sang giao diện tra cứu
        else:
            st.error("❌ Sai tên đăng nhập hoặc mật khẩu.")
else:
    # Giao diện tra cứu thuế
    st.success(f"Xin chào **{st.session_state.username}** 👋")
    st.markdown("### 🔍 Nhập mã số thuế để tra cứu:")

    tax_id = st.text_input("Mã số thuế")

    if st.button("Tra cứu"):
        if tax_id in tax_records:
            info = tax_records[tax_id]
            st.markdown("#### ✅ Kết quả tra cứu:")
            for key, value in info.items():
                st.write(f"**{key}:** {value}")
        else:
            st.warning("⚠️ Không tìm thấy mã số thuế này.")

    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()
