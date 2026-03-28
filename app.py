from flask import Flask, render_template, request, session
import random
import json
import time
import os
import paho.mqtt.client as mqtt

app = Flask(__name__)
app.secret_key = "practice-secret-key"

# MQTT configuration
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "game/guess")

mqtt_client = mqtt.Client()


def connect_mqtt():
    """Connect to the MQTT broker."""
    try:
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
        mqtt_client.loop_start()
        print(f"Connected to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}")
    except Exception as e:
        print(f"MQTT connection failed: {e}")


def publish_guess(guess_value, result_message, attempts):
    """Publish guess result to MQTT."""
    payload = {
        "timestamp_ms": int(time.time() * 1000),
        "guess": guess_value,
        "result": result_message,
        "attempts": attempts
    }

    try:
        mqtt_client.publish(MQTT_TOPIC, json.dumps(payload))
        print(f"Published to MQTT: {payload}")
    except Exception as e:
        print(f"MQTT publish failed: {e}")


def new_game():
    """Start a new game."""
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

            publish_guess(guess, message, session["attempts"])

        except ValueError:
            message = "Please enter a whole number."
            publish_guess(guess_text, message, session["attempts"])

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
    connect_mqtt()
    app.run(host="0.0.0.0", port=5000)