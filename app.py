if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    # Giao diện đăng nhập
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")

    if st.button("Đăng nhập"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Đăng nhập thành công!")
        else:
            st.error("Sai tên đăng nhập hoặc mật khẩu")
else:
    # Giao diện sau khi đăng nhập: TRA CỨU
    st.success(f"Xin chào {username} 👋")
    st.subheader("🔍 Nhập mã số thuế để tra cứu:")

    tax_id = st.text_input("Mã số thuế")

    if st.button("Tra cứu"):
        if tax_id in tax_records:
            info = tax_records[tax_id]
            st.write("### ✅ Thông tin thuế:")
            for key, value in info.items():
                st.write(f"**{key}:** {value}")
        else:
            st.warning("⚠️ Không tìm thấy mã số thuế.")
