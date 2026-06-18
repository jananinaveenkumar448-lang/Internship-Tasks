import csv
import json
students = [
    ["Janani", 85],
    ["Rahul", 92],
    ["Priya", 78]
] 
def save_to_csv(filename, data):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Score"])
        writer.writerows(data)
def load_from_csv(filename):
    students = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            students.append([row[0], int(row[1])])
    return students
def save_to_json(filename, data):
    student_dicts = []
    for name, score in data:
        student_dicts.append({
            "name": name,
            "score": score
        })
    with open(filename, "w") as file:
        json.dump(student_dicts, file, indent=4)
def load_from_json(filename):
    with open(filename, "r") as file:
        return json.load(file)
def main():
    save_to_csv("students.csv", students)
    save_to_json("students.json", students)
    print("Files saved successfully.\n")
    # Read files back
    csv_students = load_from_csv("students.csv")
    json_students = load_from_json("students.json")
    print("Data loaded from CSV:")
    for student in csv_students:
        print(student)
    print("\nData loaded from JSON:")
    for student in json_students:
        print(student)
if __name__ == "__main__":
    main()