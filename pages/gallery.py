# ---------------- Gallery ----------------
if st.session_state.active_section == "gallery":
    st.header("📸 Department Gallery")

    folder = "gallery"
    os.makedirs(folder, exist_ok=True)

    if st.session_state.staff_logged:
        uploaded = st.file_uploader("Upload event photo", type=["jpg", "png"])
        if uploaded:
            with open(f"{folder}/{uploaded.name}", "wb") as f:
                f.write(uploaded.getbuffer())
            st.success("Photo uploaded!")

    files = os.listdir(folder)
    if files:
        for img in files:
            st.image(f"{folder}/{img}", use_column_width=True)
    else:
        st.info("No photos uploaded yet.")




