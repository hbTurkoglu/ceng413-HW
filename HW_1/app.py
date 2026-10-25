import os
from flask import Flask, jsonify

app = Flask(__name__)

GREETING = os.environ.get("GREETING", "Hello from CENG413 HW1!")
DATA_DIR = os.environ.get("DATA_DIR", "/data")

@app.route("/")
def home():
    return jsonify({
        "message": GREETING,
        "data_dir": DATA_DIR
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/student")
def student():
    return jsonify({
        "course": "CENG413",
        "homework": "HW-1",
        "topic": "Containerize a Small App"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)