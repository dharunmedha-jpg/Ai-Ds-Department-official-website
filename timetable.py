
# ---------------- Year-wise Timetable ----------------
if st.session_state.active_section == "timetable":
    st.header("📝 Exam Timetable")

    base_folder = "timetable"
    os.makedirs(base_folder, exist_ok=True)

    year = st.selectbox(
        "Select Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    year_folder = os.path.join(base_folder, year)
    os.makedirs(year_folder, exist_ok=True)

    if st.session_state.staff_logged:
        uploaded = st.file_uploader(
            f"Upload timetable for {year}",
            type=["pdf"]
        )
        if uploaded:
            with open(f"{year_folder}/{uploaded.name}", "wb") as f:
                f.write(uploaded.getbuffer())
            st.success("Timetable uploaded!")

    st.subheader(f"{year} Timetables")

    files = os.listdir(year_folder)
    if files:
        for file in files:
            with open(f"{year_folder}/{file}", "rb") as f:
                st.download_button(
                    label=f"Download {file}",
                    data=f,
                    file_name=file
                )
    else:
        st.info("No timetable uploaded for this year.")

