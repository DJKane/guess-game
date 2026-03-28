import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPICS = [("game/guess", 0), ("game/result", 0), ("game/control", 0)]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    for topic, qos in TOPICS:
        client.subscribe(topic, qos)
        print(f"Subscribed to {topic}")

def on_message(client, userdata, msg):
    print(f"[RECEIVED] topic={msg.topic} payload={msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Connecting subscriber to broker...")
client.connect(BROKER, 1883, 60)
client.loop_forever()