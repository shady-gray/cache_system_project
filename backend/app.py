#Author: Basil Bassey

from flask import Flask, jsonify
from flask_cors import CORS
import database
import cache
import time

app = Flask(__name__)
CORS(app)

@app.route("/student/<int:student_id>")
def get_student(student_id):
    start = time.time()
    key = f"student:{student_id}"

    # 1️⃣ Check cache
    cached = cache.get(key)
    if cached:
        source = "cache"
        student = cached
    else:
        # 2️⃣ Fetch from "database"
        student = database.get_student(student_id)
        if not student:
            return jsonify({"error": "Student not found"}), 404

        # 3️⃣ Save to cache
        cache.set(key, student)
        source = "database"

    end = time.time()
    response_time = round(end - start, 3)

    return jsonify({
        "data": student,
        "source": source,
        "time": response_time
    })

@app.route("/stats")
def stats():
    return jsonify(cache.stats())

@app.route("/clear")
def clear_cache():
    cache.clear()
    return "Cache cleared"

if __name__ == "__main__":
    app.run(debug=True)
