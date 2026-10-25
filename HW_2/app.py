import os
import socket
import redis
from flask import Flask, jsonify, request

app = Flask(__name__)

GREETING = os.environ.get("APP_GREETING", "Hello from CENG413 HW2")
REDIS_HOST = os.environ.get("REDIS_HOST", "cache")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))

_redis = None


def get_redis():
    """Create the Redis client once."""
    global _redis
    if _redis is None:
        _redis = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True,
            socket_connect_timeout=2,
        )
    return _redis


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/greet")
def greet():
    name = request.args.get("name", "student")
    return jsonify(message=f"{GREETING}, {name}!")


@app.get("/visit")
def visit():
    client = get_redis()
    count = int(client.incr("visits"))
    return jsonify(visits=count, storage="redis", service=REDIS_HOST)


@app.get("/whoami")
def whoami():
    return jsonify(hostname=socket.gethostname())


@app.get("/notes")
def notes():
    client = get_redis()
    new_note = request.args.get("add")
    if new_note:
        client.rpush("notes", new_note)
    all_notes = client.lrange("notes", 0, -1)
    return jsonify(total=len(all_notes), notes=all_notes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)