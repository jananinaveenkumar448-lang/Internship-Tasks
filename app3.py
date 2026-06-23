from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB = "students.db"


# ---------- DATABASE INIT ----------
def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        score REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------- CREATE STUDENT ----------
@app.route("/students", methods=["POST"])
def add_student():
    data = request.json

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, score) VALUES (?, ?, ?)",
        (data["name"], data["age"], data["score"])
    )

    conn.commit()
    conn.close()

    return {"message": "Student added successfully"}


# ---------- GET ALL STUDENTS ----------
@app.route("/students", methods=["GET"])
def get_students():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "name": r[1],
            "age": r[2],
            "score": r[3]
        })

    return jsonify(result)


# ---------- GET STUDENT BY ID ----------
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "score": row[3]
        }

    return {"error": "Student not found"}, 404


# ---------- UPDATE STUDENT ----------
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name=?, age=?, score=?
        WHERE id=?
    """, (data["name"], data["age"], data["score"], id))

    conn.commit()
    conn.close()

    return {"message": "Student updated successfully"}


# ---------- DELETE STUDENT ----------
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return {"message": "Student deleted successfully"}


# ---------- RUN SERVER ----------
if __name__ == "__main__":
    app.run(debug=True)