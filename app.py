from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    user_choice = ""
    computer_choice = ""

    if request.method == "POST":
        user_choice = request.form["choice"]
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
        else:
            result = "Computer wins!"

    return render_template("index.html", result=result,
                           user_choice=user_choice,
                           computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)
