import streamlit as st
import os

st.set_page_config(page_title="AI & DS Department", layout="wide")

# ---------- Background ----------
page_bg = """
<style>
.stApp {
    background-image: url("bg.webp");
    background-size: cover;
    background-position: center;
}

.title {
    font-size: 48px;
    font-weight: bold;
    color: #00ffff;
    text-align: center;
    text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
}

.subtitle {
    font-size: 22px;
    color: white;
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Header ----------
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.image("logo.jpeg", width=80)

with col2:
    st.markdown('<div class="title">AI & DS Department</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Welcome to the official department portal</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# ---------- Staff Login ----------
if "staff_logged" not in st.session_state:
    st.session_state.staff_logged = False

with st.sidebar:
    st.header("Staff Login")

    password = st.text_input("Enter password", type="password")

    if st.button("Login"):
        if password == "admin123":
            st.session_state.staff_logged = True
            st.success("Login successful")
        else:
            st.error("Wrong password")

# ---------- Main Buttons ----------
st.header("Department Sections")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📷 Gallery"):
        st.switch_page("pages/gallery.py")

with col2:
    if st.button("🏆 Achievements"):
        st.switch_page("pages/achievements.py")

with col3:
    if st.button("📅 Events"):
        st.switch_page("pages/events.py")

with col4:
    if st.button("📝 Timetable"):
        st.switch_page("pages/timetable.py")
