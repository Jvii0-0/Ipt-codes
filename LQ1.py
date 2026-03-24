raw_student_data = "Anna, 85 | Ben, ninety | Carla, 78 | Dan,92 | Eve, | Frank, 88 | Grace, 91% | Henry, 84 | Isla, 91.5 | Jack, 74.9 | Kara, 77 | Liam, 81 | Mona,89% | Nate, 95 | Owen, -"

# Separate student records
student_records = raw_student_data.split("|")

validated_students = []

for record in student_records:
    parts = record.strip().split(",")

    name = parts[0].strip()

    if len(parts) > 1:
        score_raw = parts[1].strip()
    else:
        score_raw = ""

    if score_raw == "" or score_raw == "-":
        score = 50
    else:
        score_raw = score_raw.replace("%", "")

        if score_raw.replace(".", "").isdigit():
            score = int(float(score_raw))
        else:
            continue

    validated_students.append((name, score))

print("Cleaned Data")
for student in validated_students:
    print(student[0], "=>", student[1])

# Passing and failing
passing_students = []
failing_students = []

for student in validated_students:
    if student[1] >= 75:
        passing_students.append(student)
    else:
        failing_students.append(student)

print("\nPassing Students")
for student in passing_students:
    print(student[0], "=>", student[1])

print("\nFailing Students")
for student in failing_students:
    print(student[0], "=>", student[1])

# Total and average
total = 0
count = 0
scores = []

for student in validated_students:
    score = student[1]
    scores.append(score)
    total = total + score
    count = count + 1

average = total / count

print("\nTotal Score:", total)
print("Average Score:", average)

# Median
scores.sort()

if count % 2 == 0:
    mid = count // 2
    median = (scores[mid - 1] + scores[mid]) / 2
else:
    median = scores[count // 2]

print("Median Score:", median)

# Highest and lowest
highest = max(scores)
lowest = min(scores)

print("\nHighest Score Student/s")
for student in validated_students:
    if student[1] == highest:
        print(student[0], "=>", student[1])

print("\nLowest Score Student/s")
for student in validated_students:
    if student[1] == lowest:
        print(student[0], "=>", student[1])
