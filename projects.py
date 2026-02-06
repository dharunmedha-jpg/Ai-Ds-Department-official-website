import streamlit as st
import requests

# =============================
# SETTINGS
# =============================

API_KEY = "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"


# =============================
# PAGE TITLE
# =============================

st.title("🚀 Projects Portal")

project = st.selectbox(
    "Choose Project",
    ["Chatbot", "Hackathon", "Oneword Test"]
)


# =============================
# CHATBOT
# =============================

if project == "Chatbot":

    st.header("🤖 Mini ChatGPT (Online Free AI)")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("Ask something")

    if st.button("Send") and user_input:

        # show user message
        st.session_state.messages.append(("You", user_input))

        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": user_input}]
        }

        response = requests.post(url, headers=headers, json=data)

        answer = response.json()["choices"][0]["message"]["content"]

        st.session_state.messages.append(("Bot", answer))

    # show chat history
    for role, msg in st.session_state.messages:
        if role == "You":
            st.markdown(f"🧑 **You:** {msg}")
        else:
            st.markdown(f"🤖 **Bot:** {msg}")


# =============================
# HACKATHON
# =============================

elif project == "Hackathon":

    import random
    import time
    import pandas as pd
    import os

    st.header("🏆 Coding Quiz Hackathon (1000 Questions)")

    # ======================================================
    # 🧠 AUTO GENERATE 1000 QUESTIONS
    # ======================================================

    def generate_questions():

        questions = []

        # ---------- PYTHON ----------
        for i in range(250):
            questions.append({
                "Question": f"Which keyword is used to define function in Python? ({i})",
                "A": "def",
                "B": "fun",
                "C": "function",
                "D": "define",
                "Answer": "A"
            })

        # ---------- C LANGUAGE ----------
        for i in range(250):
            questions.append({
                "Question": f"C language main function syntax? ({i})",
                "A": "main()",
                "B": "start()",
                "C": "run()",
                "D": "init()",
                "Answer": "A"
            })

        # ---------- DSA ----------
        for i in range(250):
            questions.append({
                "Question": f"Stack follows which principle? ({i})",
                "A": "FIFO",
                "B": "LIFO",
                "C": "Random",
                "D": "Binary",
                "Answer": "B"
            })

        # ---------- AI/ML ----------
        for i in range(250):
            questions.append({
                "Question": f"AI stands for? ({i})",
                "A": "Automatic Input",
                "B": "Artificial Intelligence",
                "C": "Auto Internet",
                "D": "Advanced Index",
                "Answer": "B"
            })

        return questions


    ALL_QUESTIONS = generate_questions()


    # ======================================================
    # STUDENT LOGIN
    # ======================================================

    st.subheader("🧑‍🎓 Student Login")

    name = st.text_input("Name")
    roll = st.text_input("Roll Number")

    total_q = st.slider("Number of Questions", 10, 50, 20)


    # ======================================================
    # START QUIZ
    # ======================================================

    if st.button("Start Quiz"):

        st.session_state.start = True
        st.session_state.start_time = time.time()
        st.session_state.questions = random.sample(ALL_QUESTIONS, total_q)


    # ======================================================
    # RUN QUIZ
    # ======================================================

    if st.session_state.get("start"):

        score = 0

        for i, row in enumerate(st.session_state.questions):

            st.write(f"### Q{i+1}. {row['Question']}")

            options = [row['A'], row['B'], row['C'], row['D']]
            random.shuffle(options)

            choice = st.radio("Select:", options, key=i)

            if choice == row[row['Answer']]:
                score += 1


        if st.button("Submit Quiz"):

            end = time.time()
            taken = int(end - st.session_state.start_time)

            st.success(f"🎯 Score: {score}")
            st.write(f"⏱ Time: {taken} sec")

            # =====================================
            # SAVE LEADERBOARD
            # =====================================
            result = {
                "Name": name,
                "Roll": roll,
                "Score": score,
                "Time": taken
            }

            if os.path.exists("leaderboard.csv"):
                lb = pd.read_csv("leaderboard.csv")
                lb = pd.concat([lb, pd.DataFrame([result])])
            else:
                lb = pd.DataFrame([result])

            lb = lb.sort_values(["Score", "Time"], ascending=[False, True])
            lb.to_csv("leaderboard.csv", index=False)

            st.session_state.start = False
            st.balloons()


    # ======================================================
    # LEADERBOARD
    # ======================================================

    st.subheader("🏅 Leaderboard")

    if os.path.exists("leaderboard.csv"):
        lb = pd.read_csv("leaderboard.csv")
        st.dataframe(lb.head(10))



# =============================
# ONEWORD TEST
# =============================

# =====================================================
# 📝 ONEW0RD TEST SYSTEM
# =====================================================

elif project == "Oneword Test":

    import os
    import json
    import pandas as pd

    st.header("📝 Oneword Test Portal")

    # -------------------------------
    # Folders auto create
    # -------------------------------

    os.makedirs("oneword_tests", exist_ok=True)
    os.makedirs("accounts", exist_ok=True)

    STAFF_FILE = "accounts/staff_accounts.json"

    # -------------------------------
    # Default staff login
    # -------------------------------

    if not os.path.exists(STAFF_FILE):
        with open(STAFF_FILE, "w") as f:
            json.dump({"psr123": "psr123"}, f)

    # -------------------------------
    # Role selection
    # -------------------------------

    role = st.radio("Login As", ["Student", "Staff"])

    # =====================================================
    # 👨‍🏫 STAFF PANEL
    # =====================================================

    if role == "Staff":

        st.subheader("👨‍🏫 Staff Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        with open(STAFF_FILE) as f:
            staff_db = json.load(f)

        if st.button("Login"):

            if username in staff_db and staff_db[username] == password:
                st.session_state.staff_logged = username
                st.success("Login Successful")
            else:
                st.error("Invalid Login")

        # ---------------------------
        # Staff Dashboard
        # ---------------------------

        if "staff_logged" in st.session_state:

            st.success(f"Welcome {st.session_state.staff_logged}")

            st.divider()

            st.subheader("📤 Upload Questions (Excel)")

            year = st.selectbox("Year", ["1", "2", "3", "4"])
            week = st.text_input("Week Name (ex: week1)")

            file = st.file_uploader("Upload Excel (.xlsx)", type=["xlsx"])

            if st.button("Upload Test"):

                if file:
                    df = pd.read_excel(file)

                    # Format: Question | Answer
                    df.to_csv(f"oneword_tests/{year}_{week}.csv", index=False)

                    st.success("Test uploaded successfully")

            # ---------------------------
            # Change password
            # ---------------------------

            st.divider()
            st.subheader("🔐 Change Password")

            new_user = st.text_input("New Username")
            new_pass = st.text_input("New Password", type="password")

            if st.button("Update Account"):
                staff_db[new_user] = new_pass

                with open(STAFF_FILE, "w") as f:
                    json.dump(staff_db, f)

                st.success("Account updated")

            if st.button("Logout"):
                del st.session_state.staff_logged
                st.rerun()

    # =====================================================
    # 🎓 STUDENT PANEL
    # =====================================================

    else:

        st.subheader("🎓 Student Login")

        name = st.text_input("Enter Your Name")
        year = st.selectbox("Year", ["1", "2", "3", "4"])

        if st.button("Start Test"):

            st.session_state.student = (name, year)

        # ---------------------------
        # Student Dashboard
        # ---------------------------

        if "student" in st.session_state:

            name, year = st.session_state.student

            st.success(f"Welcome {name}")

            tests = [f for f in os.listdir("oneword_tests") if f.startswith(year)]

            if not tests:
                st.warning("No tests available")
            else:

                selected = st.selectbox("Choose Test", tests)

                if st.button("Open Test"):

                    df = pd.read_csv(f"oneword_tests/{selected}")

                    score = 0

                    st.subheader("✍️ Answer All Questions")

                    for i, row in df.iterrows():

                        ans = st.text_input(row["Question"], key=i)

                        if ans.lower() == str(row["Answer"]).lower():
                            score += 1

                    if st.button("Submit Test"):
                        st.success(f"Your Score: {score} / {len(df)}")
