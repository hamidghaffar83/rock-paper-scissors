import streamlit as st
import random

# Page settings
st.set_page_config(page_title="Rock Paper Scissors", layout="centered")

# Custom styling
st.markdown("""
    <style>
    .stRadio > div {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    .stButton {
        display: flex;
        justify-content: left;
        margin-top: 20px;
    }
    .result-box {
        margin-top: 30px;
        padding: 15px;
        border-radius: 10px;
        background-color: #f0f2f6;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🪨 📄 ✂️ Rock, Paper, Scissors")

# Instructions
st.write("Choose your move and see what the computer picks!")

# Choices
user_choice = st.radio("Select your move:", ("rock", "paper", "scissors"), horizontal=True)

# Game logic
if st.button("Play"):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    # Determine result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win! 🎉"
    else:
        result = "Computer wins! 🤖"

    # Show results
    st.markdown(f"""
    <div class="result-box">
        <p><strong>You chose:</strong> {user_choice}</p>
        <p><strong>Computer chose:</strong> {computer_choice}</p>
        <h3>{result}</h3>
    </div>
    """, unsafe_allow_html=True)
