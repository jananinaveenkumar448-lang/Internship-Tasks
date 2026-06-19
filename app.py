from flask import Flask, jsonify
def create_app():
    app = Flask(__name__)
    students = [
        {"id": 1, "name": "Kazehaya", "score": 85},
        {"id": 2, "name": "Hyeondeo", "score": 92},
        {"id": 3, "name": "Mincheol", "score": 78}
    ]
    @app.route("/")
    def home():
        return "<h2>Student API is running</h2>"
    @app.route("/students", methods=["GET"])
    def get_students():
        return jsonify(students)
    return app
app = create_app()
if __name__ == "__main__":
    app.run(debug=True)