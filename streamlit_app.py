import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Rock Paper Scissors", layout="centered")

# Inject custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f4f4f9;
    }
    .stRadio > div {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    .stButton {
        text-align: left;
        padding-top: 20px;
    }
    .stTitle {
        color: #4A90E2;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Game title
st.title("🪨 📄 ✂️ Rock, Paper, Scissors")

# Game instructions
st.write("Choose one and play against the computer!")

# User choice
user_choice = st.radio("Your choice:", ("rock", "paper", "scissors"), horizontal=True)

# Game logic
if st.button("Play"):
    comp = random.choice(["rock", "paper", "scissors"])
    st.write(f"**Computer chose:** {comp}")
    if user_choice == comp:
        st.success("It's a tie!")
    elif (user_choice == "rock" and comp == "scissors") or \
         (user_choice == "paper" and comp == "rock") or \
         (user_choice == "scissors" and comp == "paper"):
        st.success("You win! 🎉")
    else:
        st.error("You lose! 😢")
