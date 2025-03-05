import re
import streamlit as st

# Page styling
st.set_page_config(
    page_title="Password Strength Checker by Imtiaz Ali",
    page_icon="🔑", layout="centered"
)
st.markdown(
    """
    <style>
    .main {
        align-items: center;                                   
    }
    .stTextInput {
       width: 60% !important; margin: auto;
    }
    .stButton button {
       width: 50%; background-color: #f63366; color: white; font-size: 18px;
    }
    .stButton button:hover {
       background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and description
st.title("🔐 Password Strength Checker by Imtiaz Ali")
st.write("Put your password below to check its strength. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    # Check for both uppercase and lowercase letters
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain both uppercase and lowercase letters.")

    # Check for at least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one digit (0-9).")

    # Check for at least one special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one special character (!@#$%^&*).")

    # Display feedback based on score
    if score == 4:
        st.success("✅ **Password is strong** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Password is medium** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Password is weak** - Please improve security by adding more features.")

    # Show detailed feedback for improvement
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for point in feedback:
                st.write(point)

# Input and button outside the function
password = st.text_input("Enter your password", type="password", help="Enter your password to check its strength.")
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter your password first!")