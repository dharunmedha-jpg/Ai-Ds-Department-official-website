import streamlit as st
import base64
import os

st.set_page_config(layout="wide")

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

hero_img = get_base64_image("bg.webp")

# HERO SECTION
st.markdown(f"""
<style>
.hero-container {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(135deg, #0f172a, #0ea5e9);
    border-radius: 20px;
    padding: 40px;
    margin-bottom: 30px;
}}

.hero-text {{
    color: white;
    max-width: 50%;
}}

.hero-title {{
    font-size: 48px;
    font-weight: bold;
    line-height: 1.2;
}}

.hero-sub {{
    font-size: 20px;
    margin-top: 10px;
    opacity: 0.9;
}}

.hero-btn {{
    display: inline-block;
    margin-top: 20px;
    padding: 12px 24px;
    background: #1d4ed8;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    text-decoration: none;
}}

.hero-image {{
    max-width: 45%;
}}

.hero-image img {{
    width: 100%;
    border-radius: 15px;
}}
</style>

<div class="hero-container">
    <div class="hero-text">
        <div class="hero-title">
            Welcome to the<br>
            AI & Data Science Department
        </div>
        <div class="hero-sub">
            Innovating the Future with Intelligence.
        </div>
        <div class="hero-btn">Learn More</div>
    </div>
    <div class="hero-image">
        <img src="data:image/webp;base64,{hero_img}">
    </div>
</div>
""", unsafe_allow_html=True)



# ---------------- Header ----------------
st.markdown("""
<div class="hero">
    <div class="glow-text">🎓 P.S.R. ENGINEERING COLLEGE 🚀</div>
    <h2>Artificial Intelligence & Data Science Department</h2>
    <p>Welcome to the Department Portal</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Staff Login ----------------
st.markdown("---")
st.subheader("Staff Access")

if "staff_logged" not in st.session_state:
    st.session_state.staff_logged = False

if not st.session_state.staff_logged:
    if st.checkbox("Staff Login"):
        password = st.text_input("Enter staff password", type="password")
        if password == "staff123":
            st.session_state.staff_logged = True
            st.success("Logged in as staff")
        elif password:
            st.error("Wrong password")
else:
    st.success("Staff mode active")
    if st.button("Logout"):
        st.session_state.staff_logged = False

# ---------------- Section Buttons ----------------
st.markdown("---")
st.subheader("Department Sections")

col1, col2, col3, col4 = st.columns(4)

if "active_section" not in st.session_state:
    st.session_state.active_section = None

if col1.button("📸 Gallery"):
    st.session_state.active_section = "gallery"

if col2.button("🏆 Achievements"):
    st.session_state.active_section = "achievements"

if col3.button("📅 Events"):
    st.session_state.active_section = "events"

if col4.button("📝 Timetable"):
    st.session_state.active_section = "timetable"

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

# ---------------- Achievements ----------------
if st.session_state.active_section == "achievements":
    st.header("🏆 Achievements")

    folder = "achievements"
    os.makedirs(folder, exist_ok=True)

    if st.session_state.staff_logged:
        uploaded = st.file_uploader("Upload achievement image", type=["jpg", "png"])
        if uploaded:
            with open(f"{folder}/{uploaded.name}", "wb") as f:
                f.write(uploaded.getbuffer())
            st.success("Achievement uploaded!")

    files = os.listdir(folder)
    if files:
        for img in files:
            st.image(f"{folder}/{img}", use_column_width=True)
    else:
        st.info("No achievements uploaded yet.")

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
