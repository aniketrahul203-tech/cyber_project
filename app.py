from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

# Database Connection (works for BOTH local + online)
db = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", "AniRahul12@*"),
    database=os.environ.get("DB_NAME", "cyber_db")
)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Incidents Page (JOIN query)
@app.route('/incidents')
def incidents():
    cursor = db.cursor()

    cursor.execute("""
    SELECT i.incident_id, t.threat_name, v.description, i.risk_score, i.status
    FROM Incident i
    JOIN Threat t ON i.threat_id = t.threat_id
    JOIN Vulnerability v ON i.vulnerability_id = v.vulnerability_id
    """)

    data = cursor.fetchall()
    return render_template("incidents.html", data=data)

# Run App
if __name__ == "__main__":
    app.run(debug=True)
