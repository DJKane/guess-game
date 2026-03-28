from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "practice-secret-key"


def new_game():
    session["target"] = random.randint(1, 20)
    session["attempts"] = 0
    session["message"] = "I picked a number between 1 and 20."


@app.route("/", methods=["GET", "POST"])
def index():
    if "target" not in session:
        new_game()

    if request.method == "POST":
        if "restart" in request.form:
            new_game()
            return render_template(
                "index.html",
                message=session["message"],
                attempts=session["attempts"]
            )

        guess_text = request.form.get("guess", "").strip()

        try:
            guess = int(guess_text)
            session["attempts"] += 1

            if guess < session["target"]:
                message = "Too low. Try again."
            elif guess > session["target"]:
                message = "Too high. Try again."
            else:
                message = f"Correct! You got it in {session['attempts']} attempts."
        except ValueError:
            message = "Please enter a whole number."

        return render_template(
            "index.html",
            message=message,
            attempts=session["attempts"]
        )

    return render_template(
        "index.html",
        message=session["message"],
        attempts=session["attempts"]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)