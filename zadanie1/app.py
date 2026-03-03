import os
import time
from flask import Flask, request, jsonify
import psycopg2

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASS = os.getenv("DB_PASS", "apppass")
DB_PORT = int(os.getenv("DB_PORT", "5432"))

app = Flask(__name__)

def get_conn(retries=30, delay=2):
    last_err = None
    for _ in range(retries):
        try:
            return psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
        except Exception as e:
            last_err = e
            time.sleep(delay)
    raise last_err

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/write", methods=["POST"])
def write():
    data = request.get_json()
    conn = get_conn()
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(
            "create table if not exists messages (id serial primary key, content text)"
        )
        cur.execute(
            "insert into messages(content) values(%s) returning id",
            (data["content"],)
        )
        mid = cur.fetchone()[0]
    return {"id": mid}

@app.route("/list")
def list_messages():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("select id, content from messages order by id desc limit 50")
        rows = cur.fetchall()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

