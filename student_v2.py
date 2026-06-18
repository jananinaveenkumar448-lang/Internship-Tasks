import logging
logging.basicConfig(
    filename="student_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class ScoreError(Exception):
    pass
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def validate(self):
        if not self.name or not self.name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(self.marks, list):
            raise TypeError("Marks must be a list")
        for mark in self.marks:
            if not isinstance(mark, (int, float)):
                raise TypeError("Each mark must be a number")
            if mark < 0 or mark > 100:
                raise ScoreError("Mark must be between 0 and 100")
    def calculate(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        return total, avg
try:
    name = input("Enter student name: ")
    marks = []
    for i in range(3):
        mark = float(input(f"Enter mark {i+1}: "))
        marks.append(mark)
    student = Student(name, marks)
    student.validate()
except ValueError as ve:
    print("ValueError:", ve)
    logging.error(ve)
except TypeError as te:
    print("TypeError:", te)
    logging.error(te)
except ScoreError as se:
    print("ScoreError:", se)
    logging.error(se)
else:
    total, avg = student.calculate()

    print("\n--- STUDENT DETAILS ---")
    print("Name:", name)
    print("Total:", total)
    print("Average: {:.2f}".format(avg))
    with open("students.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Total: {total}\n")
        f.write(f"Average: {avg:.2f}\n")
        f.write("-------------------\n")
finally:
    try:
        with open("students.txt", "r") as f:
            print("\n--- FILE CONTENT ---")
            print(f.read())
    except FileNotFoundError as fe:
        print("File not found!")
        logging.error(fe)
    print("\nProgram execution completed.")