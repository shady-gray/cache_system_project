#Author: Basil Bassey

from flask import Flask, jsonify
from flask_cors import CORS
import database  # import your fake database
import time

app = Flask(__name__)
CORS(app)

@app.route("/student/<int:student_id>")
def get_student(student_id):
    start = time.time()  # start timer

    student = database.get_student(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    end = time.time()  # end timer
    response_time = round(end - start, 3)

    return jsonify({
        "data": student,
        "source": "database",
        "time": response_time
    })

if __name__ == "__main__":
    app.run(debug=True)
