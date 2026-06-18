import csv
from collections import Counter
students = []
with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "name": row["Name"],
            "score": float(row["Score"])
        })
ranked = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)
average = sum(
    student["score"] for student in students
) / len(students)
top_three = ranked[:3]
bottom_three = ranked[-3:]
score_counter = Counter(
    student["score"] for student in students
)
print("\n===== STUDENT LEADERBOARD =====")
print(f"{'Rank':<6}{'Name':<15}{'Score':<10}")
for rank, student in enumerate(ranked, start=1):
    print(
        f"{rank:<6}"
        f"{student['name']:<15}"
        f"{student['score']:<10}"
    )
print("\nAverage Score:", round(average, 2))
print("\n--- TOP 3 STUDENTS ---")
for student in top_three:
    print(f"{student['name']} : {student['score']}")
print("\n--- BOTTOM 3 STUDENTS ---")
for student in bottom_three:
    print(f"{student['name']} : {student['score']}")
print("\n--- SCORE FREQUENCY ---")
for score, count in score_counter.items():
    print(f"{score}: {count}")