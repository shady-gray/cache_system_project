#Author: Basil Bassey

import time

# Simulated student database
STUDENTS = {
    1: {"id": 1, "name": "Basil", "dept": "CSC"},
    2: {"id": 2, "name": "Chika", "dept": "CSC"},
    3: {"id": 3, "name": "Chinaza", "dept": "Physics"},
    4: {"id": 4, "name": "Burabari", "dept": "Engineering"}
}

# Function to simulate a slow database call
def get_student(student_id):
    time.sleep(10)  # simulate slow DB (2 seconds)
    return STUDENTS.get(student_id)
