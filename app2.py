from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/add-student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"].strip()
        age = request.form["age"].strip()
        department = request.form["department"].strip()

        if not name:
            return render_template(
                "add_student.html",
                message="Name cannot be empty"
            )

        try:
            age = int(age)
        except ValueError:
            return render_template(
                "add_student.html",
                message="Age must be a number"
            )

        if age < 1 or age > 100:
            return render_template(
                "add_student.html",
                message="Age must be between 1 and 100"
            )

        with open("student_details.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, department])

        return render_template(
            "add_student.html",
            message="Student Added Successfully!"
        )

    return render_template("add_student.html")


if __name__ == "__main__":
    app.run(debug=True)