raw_student_data = "Anna, 85 | Ben, ninety | Carla, 78 | Dan,92 | Eve, | Frank, 88 | Grace, 91% | Henry, 84 | Isla, 91.5 | Jack, 74.9 | Kara, 77 | Liam, 81 | Mona,89% | Nate, 95 | Owen, -"

students_data = raw_student_data.split("|")

for rows in students_data:
    parts = rows.strip().split(",")

    name = parts[0]

    if len(rows) >= 1:
        raw_scores = parts[1].strip()
    else:
        raw_scores = ""

    if raw_scores == "" or raw_scores == "-":
        score = 50
    else:
        score = raw_scores.replace("%", "")

        if raw_scores.replace(".", "").isdigit():
            score = int(float(raw_scores))
        else:
            continue
    print(name)
    print(score)
