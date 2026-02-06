# ---------------- Events ----------------
if st.session_state.active_section == "events":
    st.header("📅 Upcoming Events")

    folder = "events"
    os.makedirs(folder, exist_ok=True)

    if st.session_state.staff_logged:
        uploaded = st.file_uploader("Upload event poster", type=["jpg", "png"])
        if uploaded:
            with open(f"{folder}/{uploaded.name}", "wb") as f:
                f.write(uploaded.getbuffer())
            st.success("Event uploaded!")

    files = os.listdir(folder)
    if files:
        for img in files:
            st.image(f"{folder}/{img}", use_column_width=True)
    else:
        st.info("No events uploaded yet.")
