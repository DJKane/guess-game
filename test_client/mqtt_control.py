import paho.mqtt.client as mqtt
import json
import time

BROKER = "localhost"

client = mqtt.Client()

print("Connecting to broker...")
client.connect(BROKER, 1883, 60)
client.loop_start()

time.sleep(1)

payload = {
    "command": "reset"
}

client.publish("game/control", json.dumps(payload))
print(f"Published to game/control: {payload}")

time.sleep(1)

client.loop_stop()
client.disconnect()
