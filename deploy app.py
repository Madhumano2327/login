import streamlit as st

# Student credentials (replace with a secure database in a real application)
student_credentials = {
    "john": "password123",
    "jane": "password456",
}

def login_page():
    st.title("Student Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in student_credentials and student_credentials[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            # Add logic to redirect to student dashboard
        else:
            st.error("Invalid username or password")

def student_dashboard():
    st.title(f"Welcome, {st.session_state.username}!")
    # Add student dashboard content here

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        student_dashboard()
    else:
        login_page()

if _name_ == "_main_":
    main()
