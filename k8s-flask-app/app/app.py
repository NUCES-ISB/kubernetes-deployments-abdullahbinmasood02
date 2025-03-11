from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "flaskdb")
DB_USER = os.environ.get("DB_USER", "flaskuser")
DB_PASS = os.environ.get("DB_PASS", "flaskpassword")

@app.route("/")
def hello():
    return "Flask App Running on Kubernetes!"

@app.route("/db")
def check_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST
        )
        return "Connected to PostgreSQL!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
