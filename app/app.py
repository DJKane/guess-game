from flask import Flask, render_template, request
from mqtt_client import connect_mqtt, publish_message

app = Flask(__name__)

SECRET_NUMBER = 42

connect_mqtt()

@app.route("/", methods=["GET", "POST"])
def index():
    result_message = ""

    if request.method == "POST":
        player = request.form.get("player", "local")
        guess_raw = request.form.get("guess", "")

        try:
            guess = int(guess_raw)

            guess_payload = {
                "player": player,
                "guess": guess
            }
            publish_message("game/guess", guess_payload)

            if guess < SECRET_NUMBER:
                result = "too low"
            elif guess > SECRET_NUMBER:
                result = "too high"
            else:
                result = "correct"

            result_payload = {
                "player": player,
                "guess": guess,
                "result": result
            }
            publish_message("game/result", result_payload)

            result_message = f"Your guess was {guess}: {result}"

        except ValueError:
            result_message = "Please enter a valid number."

    return render_template("index.html", result_message=result_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)