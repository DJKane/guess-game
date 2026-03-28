import json
import os
import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", 1883))

client = mqtt.Client()

def connect_mqtt():
    try:
        client.connect(BROKER, PORT, 60)
        client.loop_start()
        print(f"Connected to MQTT broker at {BROKER}:{PORT}")
    except Exception as e:
        print(f"MQTT connection failed: {e}")

def publish_message(topic, payload):
    try:
        message = json.dumps(payload)
        client.publish(topic, message)
        print(f"Published to {topic}: {message}")
    except Exception as e:
        print(f"Publish failed: {e}")