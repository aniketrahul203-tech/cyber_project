# 🔐 Cybersecurity Incident Response System

## 📌 Project Overview
This project is a web-based Cybersecurity Incident Response System developed using Flask and MySQL. It helps manage and analyze cybersecurity events, alerts, threats, vulnerabilities, and mitigation actions.

---

## 🛠 Technologies Used
- Python (Flask)
- MySQL
- HTML, CSS
- Git & GitHub

---

## 📂 Database Design
The system includes:
- Event
- Alert (Weak Entity)
- Threat
- Vulnerability
- Mitigation Actions

---

## 🔗 Relationships
- Alert depends on Event (Weak Entity)
- Alerts trigger Mitigation Actions
- Threats exploit Vulnerabilities

---

## 📊 Features
- Track cybersecurity incidents  
- Analyze risk levels  
- Display incidents using SQL JOIN queries  
- Simple web interface  

---

## 📸 Screenshots

### 🔑 Dashboard
<img src="screenshots/dashboard.png" width="800"/>

---

## ▶️ How to Run

### Install dependencies:
```bash
pip install flask mysql-connector-python 
 Run the app:
   python app.py
Open browser:
http://127.0.0.1:5000

 ## 📸 OUTPUT
### Dashboard
<img src="screenshots/dashboard.png" width="800"/>


👨‍💻 Author

Rahul Kumar