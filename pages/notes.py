import streamlit as st
import os
import json

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(page_title="PSR Study Materials", layout="wide")

st.title("📚 PSR Study Materials Portal")

# =====================================
# FOLDERS
# =====================================
BASE_FOLDER = "notes_data"
ACCOUNT_FILE = "accounts/staff_accounts.json"

os.makedirs(BASE_FOLDER, exist_ok=True)
os.makedirs("accounts", exist_ok=True)

# =====================================
# DEFAULT ACCOUNT (first time only)
# =====================================
if not os.path.exists(ACCOUNT_FILE):
    with open(ACCOUNT_FILE, "w") as f:
        json.dump({"psr123": "psr123"}, f)


# =====================================
# ACCOUNT FUNCTIONS
# =====================================
def load_accounts():
    with open(ACCOUNT_FILE, "r") as f:
        return json.load(f)


def save_accounts(data):
    with open(ACCOUNT_FILE, "w") as f:
        json.dump(data, f, indent=4)


# =====================================
# SESSION
# =====================================
if "staff_logged" not in st.session_state:
    st.session_state.staff_logged = False

if "staff_user" not in st.session_state:
    st.session_state.staff_user = ""


# =====================================
# SIDEBAR LOGIN
# =====================================
st.sidebar.header("🔐 Staff Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    accounts = load_accounts()

    if username in accounts and accounts[username] == password:
        st.session_state.staff_logged = True
        st.session_state.staff_user = username
        st.sidebar.success("Logged in as staff ✅")
    else:
        st.sidebar.error("Invalid login ❌")


if st.session_state.staff_logged:
    if st.sidebar.button("Logout"):
        st.session_state.staff_logged = False
        st.rerun()


# =====================================
# MAIN FILTERS
# =====================================
# ---------- Year ----------
# ---------- Layout columns ----------
# =========================
# FILTERS (TOP)
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    year = st.selectbox("🎓 Year", ["1st_year","2nd_year","3rd_year","4th_year"])

with col2:
    sem_map = {
        "1st_year": ["Sem1","Sem2"],
        "2nd_year": ["Sem3","Sem4"],
        "3rd_year": ["Sem5","Sem6"],
        "4th_year": ["Sem7","Sem8"]
    }
    semester = st.selectbox("📘 Semester", sem_map[year])

with col3:
    subject_map = {
        "1st_year": ["Tamil","English","Maths","Physics","Chemistry"],
        "2nd_year": ["DSA","OOPS","DBMS","OS","Python"],
        "3rd_year": ["AI","ML","CN","Cloud"],
        "4th_year": ["Project","Elective","Big Data"]
    }
    subject = st.selectbox("📗 Subject", subject_map[year])


# =========================
# AVAILABLE NOTES (ONLY ONE PLACE)
# =========================
st.subheader("📂 Available Notes")

folder_path = f"notes/{year}/{semester}/{subject}"

import os

# ✅ AUTO CREATE FOLDER (BEST WAY)
os.makedirs(folder_path, exist_ok=True)

files = os.listdir(folder_path)

if files:
    for f in files:
        st.write("📄", f)
else:
    st.info("No notes uploaded yet.")

# =====================================
# STAFF UPLOAD SECTION
# =====================================
if st.session_state.staff_logged:

    st.success(f"Logged in as staff: {st.session_state.staff_user}")

    st.subheader("📤 Upload Notes (PDF only)")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        save_path = os.path.join(folder_path, uploaded_file.name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success("✅ File uploaded successfully")

    # =====================================
    # CHANGE PASSWORD SECTION
    # =====================================
    st.divider()
    st.subheader("🔐 Change Username / Password")

    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Update Account"):

        if new_user and new_pass:

            accounts = load_accounts()

            old_user = st.session_state.staff_user

            accounts.pop(old_user)
            accounts[new_user] = new_pass

            save_accounts(accounts)

            st.success("Account updated! Please login again")

            st.session_state.staff_logged = False
            st.rerun()


# =====================================
# STUDENT VIEW FILES
# =====================================

files = os.listdir(folder_path)

if files:
    for file in files:
        with open(os.path.join(folder_path, file), "rb") as f:
            st.download_button(
                label=f"📄 {file}",
                data=f,
                file_name=file
            )

