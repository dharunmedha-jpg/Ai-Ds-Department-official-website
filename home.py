import streamlit as st

st.set_page_config(page_title="AI & DS Department", layout="wide")

# Background image
page_bg = """
<style>
.stApp {
    background-image: url("bg.webp");
    background-size: cover;
    background-position: center;
}
.title {
    font-size: 45px;
    font-weight: bold;
    color: white;
    text-align: center;
    text-shadow: 0 0 15px #00ffff;
}
.subtitle {
    font-size: 25px;
    color: #eeeeee;
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Header
st.markdown('<div class="title">AI & DS Department</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Welcome to the official department portal</div>', unsafe_allow_html=True)

st.write("")
st.write("")

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
