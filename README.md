<div align="center">

# 🚗 GuardianTrack AI

### Intelligent Vehicle Tracking & Theft Prevention System

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask">
<img src="https://img.shields.io/badge/ESP32-IoT-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/GPS-Tracking-red?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">

<br><br>

<img src="https://raw.githubusercontent.com/shravanisahare14-web/IoT-Vehicle-Tracking-Theft-Prevention-System/main/images/dashboard.png" width="95%">

### 📍 Monitor • 🛡️ Protect • 📊 Analyze

An IoT-inspired Vehicle Tracking and Theft Prevention System that combines GPS tracking, geofence monitoring, threat detection, analytics, and reporting into a unified intelligent dashboard.

</div>

---

# 🌟 Project Highlights

✨ Real-Time Vehicle Tracking

✨ Interactive GPS Dashboard

✨ Geofence Breach Detection

✨ Threat Monitoring System

✨ Route Visualization

✨ Vehicle Analytics Dashboard

✨ PDF Report Generation

✨ CSV Data Export

✨ ESP32 Hardware Support

✨ Python Simulation Support

---

# 🎯 Problem Statement

Vehicle theft and unauthorized vehicle movement continue to be major security concerns.

Traditional tracking solutions often lack centralized monitoring, intelligent threat detection, visual route tracking, and analytical insights.

GuardianTrack AI addresses these challenges through a modern vehicle monitoring platform that enhances visibility, security, and operational awareness.

---

# 📸 Project Preview

## 🚘 Dashboard

<p align="center">
<img src="https://raw.githubusercontent.com/shravanisahare14-web/IoT-Vehicle-Tracking-Theft-Prevention-System/main/images/dashboard.png" width="90%">
</p>

### Dashboard Features

* Live GPS Coordinates
* Vehicle Speed Monitoring
* Engine Status Tracking
* Geofence Monitoring
* Threat Detection
* Route Visualization

---

## 📊 Analytics Center

<p align="center">
<img src="https://raw.githubusercontent.com/shravanisahare14-web/IoT-Vehicle-Tracking-Theft-Prevention-System/main/images/analytics.png" width="90%">
</p>

### Analytics Features

* Total Distance Travelled
* Average Speed Analysis
* Threat Event Statistics
* Breach Monitoring
* Historical Insights
* Interactive Visualizations

---

# 🏗️ System Architecture

```text
         GPS Module
              │
              ▼
      Vehicle Location Data
              │
              ▼
       Tracking Engine
              │
              ▼
     Geofence Analysis
              │
              ▼
      Threat Detection
              │
              ▼
      Analytics Engine
              │
              ▼
        Flask Backend
              │
              ▼
    Interactive Dashboard
              │
      ┌───────┴───────┐
      ▼               ▼
 PDF Reports     CSV Reports
```

---

# ⚡ Technology Stack

| Category        | Technologies          |
| --------------- | --------------------- |
| Backend         | Python, Flask         |
| Frontend        | HTML, CSS, JavaScript |
| Visualization   | Leaflet.js, Chart.js  |
| Data Processing | JSON, Pandas          |
| Reporting       | ReportLab, CSV Export |
| Hardware        | ESP32, NEO-6M GPS     |

---

# 🚀 Core Functionalities

## 📍 Vehicle Tracking

Track and visualize vehicle movement using GPS location data.

## 🛡️ Geofence Monitoring

Detect when a vehicle moves beyond predefined boundaries.

## 🚨 Threat Detection

Monitor suspicious activity and identify security breaches.

## 📊 Analytics Dashboard

Generate actionable insights using distance, speed, and threat statistics.

## 📄 Reporting Engine

Export operational data into professional PDF and CSV reports.

---

# 📂 Project Structure

```text
GuardianTrack-AI/

├── arduino_code/
│   └── guardiantrack_esp32.ino
│
├── python_simulation/
│   └── gps_simulator.py
│
├── dashboard/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── data/
│   ├── latest_location.json
│   └── analytics.json
│
├── images/
│   ├── dashboard.png
│   └── analytics.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🔧 Hardware Configuration

### Components Used

* ESP32 Development Board
* NEO-6M GPS Module
* Wi-Fi Connectivity

### Basic Wiring

```text
ESP32            GPS Module

3.3V ---------- VCC
GND ----------- GND
GPIO16 -------- TX
GPIO17 -------- RX
```

---

# ▶️ Getting Started

### Clone Repository

```bash
git clone https://github.com/shravanisahare14-web/IoT-Vehicle-Tracking-Theft-Prevention-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run GPS Simulator

```bash
python python_simulation/gps_simulator.py
```

### Launch Dashboard

```bash
python dashboard/app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

# 📚 Skills Demonstrated

✅ IoT System Design

✅ GPS Tracking Concepts

✅ Geofencing Implementation

✅ Flask Web Development

✅ REST API Development

✅ Dashboard Engineering

✅ Data Visualization

✅ Report Generation

✅ Git & GitHub Workflow

---

# 🔮 Future Enhancements

* Live GPS Hardware Integration
* Mobile Application Support
* Cloud Database Storage
* Real-Time Notifications
* Fleet Management System
* Multi-Vehicle Monitoring
* AI-Based Threat Prediction

---

<div align="center">

# 👩‍💻 Author

### Shravani Sahare

**B.Tech – Electronics & Communication Engineering (ECE)**

Passionate about IoT • Embedded Systems • Artificial Intelligence • Automation

⭐ If you found this project interesting, consider giving it a star.

</div>
