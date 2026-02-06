import streamlit as st

st.set_page_config(page_title="Contacts", page_icon="📞")

st.title("Contact Us")


name = st.text_input("Name")
email = st.text_input("Your Email")
msg = st.text_area("Message")

# 🔴 CHANGE THESE
YOUR_EMAIL = "dharunmedha@gmail.com"
APP_PASSWORD = "gebolufxnfpzhjql"


def send_email(name, email, msg):

    message = EmailMessage()

    message["Subject"] = "New Contact Message from Website"
    message["From"] = YOUR_EMAIL
    message["To"] = "dharunmedha@gmail.com"

    message.set_content(
        f"""
Name: {name}
Student Email: {email}

Message:
{msg}
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(YOUR_EMAIL, APP_PASSWORD)
        server.send_message(message)


if st.button("Send"):

    if name and msg:
        send_email(name, email, msg)
        st.success("✅ Message sent to admin email!")
    else:
        st.error("Fill all fields")

