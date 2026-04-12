from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# ✅ Connect to LOCAL MySQL
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="AniRahul12@*",   # your password
        database="cyber_db"
    )
    print("✅ Connected to MySQL")
except Exception as e:
    print("❌ Database connection error:", e)
    db = None


# 🏠 HOME PAGE
@app.route('/')
def home():
    return render_template("index.html")


# 🚨 INCIDENTS PAGE
@app.route('/incidents')
def incidents():
    if not db:
        return "Database not connected"

    cursor = db.cursor()

    try:
        # 🔗 JOIN query (important for project marks)
        query = """
        SELECT 
            i.incident_id,
            t.threat_name,
            v.description,
            i.risk_score,
            i.status
        FROM Incident i
        JOIN Threat t ON i.threat_id = t.threat_id
        JOIN Vulnerability v ON i.vulnerability_id = v.vulnerability_id
        """

        cursor.execute(query)
        data = cursor.fetchall()

    except Exception as e:
        return f"Error: {e}"

    return render_template("incidents.html", data=data)


# ▶️ RUN APP
if __name__ == "__main__":
    app.run(debug=True)
