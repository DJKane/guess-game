import paho.mqtt.client as mqtt
import json
import time

BROKER = "localhost"

client = mqtt.Client()

print("Connecting publisher to broker...")
client.connect(BROKER, 1883, 60)
client.loop_start()

time.sleep(1)

guess_payload = {
    "player": "local",
    "guess": 42
}

result_payload = {
    "player": "local",
    "guess": 42,
    "result": "too low"
}

client.publish("game/guess", json.dumps(guess_payload))
print(f"Published to game/guess: {guess_payload}")

time.sleep(1)

client.publish("game/result", json.dumps(result_payload))
print(f"Published to game/result: {result_payload}")

time.sleep(1)
client.loop_stop()
client.disconnect()