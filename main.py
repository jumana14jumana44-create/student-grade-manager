students = []

with open("students.txt", "r") as s:
    lines = s.readlines()

for line in lines:
    parts = line.strip().split(",")
    student = {
        "name": parts[0],
        "math": int(parts[1]),
        "svt": int(parts[2]),
        "art": int(parts[3]),
        "music": int(parts[4]),
        "age": int(parts[5])
    }
    students.append(student)


def calculate_grade(student):
    grade = (student["math"] + student["svt"] + student["art"] + student["music"]) / 4

    assert grade > 0, "Grade must be positive"

    return grade


def check_grade(student):
    grade = calculate_grade(student)

    if grade >= 50:
        return f"{student['name']} | Age: {student['age']} | Grade: {grade} | ✅ Passed!"
    else:
        return f"{student['name']} | Age: {student['age']} | Grade: {grade} | ❌ Failed!"


for s in students:
    print(check_grade(s))


with open("results.txt", "w") as f:
    for s in students:
        f.write(check_grade(s) + "\n")
