# 🎯 Guess Game (Flask + Docker + MQTT)

A simple web-based "Guess the Number" game built with Python Flask and containerized using Docker.
This version includes MQTT publishing to demonstrate an event-driven architecture similar to real-world IIoT systems.

---

## 🚀 Overview

This project started as a basic Flask application and was extended to include:

* Docker containerization
* Docker Hub image publishing
* MQTT event streaming
* Multi-container orchestration using Docker Compose

It serves as a **learning foundation for modern application deployment and industrial data pipelines**.

---

## 🧱 Tech Stack

* Python 3.12
* Flask
* Docker
* Docker Compose
* Eclipse Mosquitto (MQTT broker)

---

## ⚙️ Features

* Random number game (1–20)
* User input via browser
* Feedback: too high / too low / correct
* Attempt tracking
* Restart game
* MQTT publishing on each guess
* Containerized and portable

---

## 📡 MQTT Integration

Each guess publishes a message to:

```text
game/guess
```

Example payload:

```json
{
  "timestamp_ms": 1710000000000,
  "guess": 12,
  "result": "Too high. Try again.",
  "attempts": 3
}
```

This simulates a **machine event stream**, similar to industrial telemetry.

---

## ▶️ Run Options

### 🟢 Option 1 — Run App Only (No MQTT)

```bash
docker run --rm -p 5000:5000 davidkane59/guess-game:1.1
```

Open:

```
http://localhost:5000
```

⚠️ Note: MQTT publishing will be disabled unless a broker is available.

---

### 🔵 Option 2 — Run Full Stack (Recommended)

```bash
docker compose up --build
```

This starts:

* Flask game
* Mosquitto MQTT broker

Open:

```
http://localhost:5000
```

---

## 🔍 View MQTT Messages

In another terminal:

```bash
docker compose exec mqtt mosquitto_sub -t game/guess -v
```

Play the game and watch live messages.

---

## 🛠️ Build Locally

```bash
git clone https://github.com/DJKane/guess-game.git
cd guess-game

docker build -t guess-game .
docker run -p 5000:5000 guess-game
```

---

## 📁 Project Structure

```
guess-game/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── mosquitto.conf
├── README.md
└── templates/
    └── index.html
```

---

## 📦 Docker Hub

Image available at:

```
https://hub.docker.com/r/davidkane59/guess-game
```

---

## 🔄 Versioning

| Tag    | Description                         |
| ------ | ----------------------------------- |
| 1.0    | Initial Flask game                  |
| 1.1    | Added MQTT + Docker Compose support |
| latest | Current stable version              |

---

## 🧠 Architecture

```
Browser → Flask App → MQTT → Broker → Subscribers
```

This mirrors a basic **Unified Namespace (UNS)** pattern used in industrial systems:

```
Machine → MQTT → Data Platform → Analytics
```

---

## 🎯 Purpose

This project demonstrates:

* Python web application basics
* Containerized deployment
* Event-driven design using MQTT
* Transition from simple app → distributed system

It provides a stepping stone toward:

* IIoT edge devices
* Machine monitoring systems
* Data pipelines (MQTT → InfluxDB → Grafana)

---

## 📌 Future Improvements

* Add Node-RED dashboard
* Store data in InfluxDB
* Visualize in Grafana
* Add difficulty levels
* Improve UI styling (CSS)
* Add persistent scoring

---

## 👤 Author

David Kane
Kane Engineering Group Inc.

---

## ⚠️ Notes

* Flask development server is used (not production-ready)
* MQTT is optional in standalone mode
* Docker Compose is the recommended deployment method

---

## 🚀 Next Steps

Extend this project into a full IIoT stack:

* MQTT → Node-RED → InfluxDB → Grafana
* Add REST API endpoints
* Deploy to edge hardware (PLCnext, industrial PC)

---
