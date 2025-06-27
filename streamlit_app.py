import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors")

st.title("🪨 📄 ✂️ Rock, Paper, Scissors Game")
st.write("Choose one and play against the computer!")

user_choice = st.radio("Your choice:", ("rock", "paper", "scissors"))
if st.button("Play"):
    comp = random.choice(["rock", "paper", "scissors"])
    st.write(f"**Computer chose:** {comp}")
    if user_choice == comp:
        st.success("It's a tie!")
    elif (user_choice=="rock" and comp=="scissors") or \
         (user_choice=="paper" and comp=="rock") or \
         (user_choice=="scissors" and comp=="paper"):
        st.success("You win! 🎉")
    else:
        st.error("You lose! 😢")
