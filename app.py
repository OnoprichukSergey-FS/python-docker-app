from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Docker basics",
        "completed": True
    },
    {
        "id": 2,
        "title": "Deploy Python app with Docker",
        "completed": False
    }
]

@app.route("/")
def home():
    return jsonify({
        "message": "Python Docker API is running",
        "status": "success",
        "routes": ["/health", "/tasks"]
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/tasks")
def get_tasks():
    return jsonify({
        "count": len(tasks),
        "tasks": tasks
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)