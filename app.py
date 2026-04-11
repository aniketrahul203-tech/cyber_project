import os
from flask import Flask, render_template
import mysql.connector
from urllib.parse import urlparse

app = Flask(__name__)

# ---------------- DB CONNECTION ----------------
db = None

try:
    db_url = os.environ.get("DATABASE_URL")

    if db_url:
        url = urlparse(db_url)

        db = mysql.connector.connect(
            host=url.hostname,
            user=url.username,
            password=url.password,
            database=url.path[1:],
            port=url.port
        )
        print("✅ Connected to Railway MySQL")

    else:
        print("❌ DATABASE_URL not found")

except Exception as e:
    print("❌ DB Error:", e)


# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return "<h2>Cybersecurity Incident Response System 🚀</h2><a href='/incidents'>View Incidents</a>"


@app.route('/incidents')
def incidents():
    if not db:
        return "❌ Database not connected"

    cursor = db.cursor()

    try:
        query = """
        SELECT i.incident_id, t.threat_name, v.description, i.risk_score, i.status
        FROM Incident i
        JOIN Threat t ON i.threat_id = t.threat_id
        JOIN Vulnerability v ON i.vulnerability_id = v.vulnerability_id
        """
        cursor.execute(query)
        data = cursor.fetchall()

    except Exception as e:
        return f"❌ Error: {e}"

    # simple HTML output
    html = "<h2>Incident List</h2><table border='1'><tr><th>ID</th><th>Threat</th><th>Vulnerability</th><th>Risk</th><th>Status</th></tr>"

    for row in data:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"

    html += "</table><br><a href='/'>Back</a>"

    return html


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
