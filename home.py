import streamlit as st

# Set page config for a modern look
st.set_page_config(page_title="Tutoring Signup Form", page_icon="🌱", layout="centered")

# Custom CSS for city background
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        height: 100% !important;
        min-height: 100% !important;
        background: url('MyImages/image.png') no-repeat center center fixed !important;
        background-size: cover !important;
        background-blend-mode: lighten;
    }
    .stApp {
        background: transparent !important;
        color: #222;
        z-index: 1;
    }
    .stTextInput > div > div > input {
        background-color: #f5fff0cc;
        border: 2px solid #7ec850;
        border-radius: 10px;
        color: #222;
        font-size: 1.1em;
    }
    .stButton > button {
        background: linear-gradient(90deg, #7ec850 0%, #b2f7ef 100%);
        color: #222;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        font-size: 1.1em;
        box-shadow: 0 2px 8px #b2f7ef55;
        transition: 0.2s;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #b2f7ef 0%, #7ec850 100%);
        color: #1b2d13;
    }
    .stSuccess {
        background-color: #e0ffe0cc !important;
        color: #2e4d25 !important;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌞 Tutoring Signup Form")
st.write("<span style='font-size:1.2em;'>Please fill out the form below to sign up for tutoring. Embrace the future with a solarpunk spirit! 🌱</span>", unsafe_allow_html=True)

first_last_name = st.text_input("First and last name")
background = st.text_input("Background")
courses = st.text_input("List of courses")
email = st.text_input("Email Address")
last_name = st.text_input("Last name")

if st.button("Submit"):
    st.success(f"Thank you for signing up, {first_last_name}! 🌻")
    st.write("We have received your information:")
    st.write(f"**Background:** {background}")
    st.write(f"**List of courses:** {courses}")
    st.write(f"**Email Address:** {email}")
    st.write(f"**Last name:** {last_name}")