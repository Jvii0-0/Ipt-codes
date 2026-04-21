class Person:
    def __init__(self, name, age):

        # Check if name is empty
        if name.strip() == "":
            print("Invalid name. Setting to 'Unknown'")
            self.name = "Unknown"  # default value if invalid
        else:
            self.name = name  # assign valid name

        # Validate age input
        try:
            age = int(age)  # convert age to integer

            # check if age is within valid range
            if 1 <= age <= 100:
                self.age = age
            else:
                print("Invalid age. Setting to 0")
                self.age = 0  # default invalid value

        except:
            print("Age must be numeric. Setting to 0")
            self.age = 0  # fallback if conversion fails

    def display_info(self):
        # display basic person info
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, student_id, course, grades):
        super().__init__(name, age)  # inherit Person attributes

        self.__student_id = student_id  # private student ID
        self.course = course  # course enrolled
        self.__grades = []  # list to store valid grades

        # process each grade input
        for grade in grades:
            self.add_grade(grade)  # validate and add grade

    def add_grade(self, grade):
        try:
            grade = float(grade)  # convert grade to float

            # validate grade range
            if 0 <= grade <= 100:
                self.__grades.append(grade)  # store valid grade

        except:
            pass  # ignore invalid input

    def get_grades(self):
        # return list of grades
        return self.__grades

    def compute_average(self):
        # return 0 if no grades exist
        if len(self.__grades) == 0:
            return 0

        # compute average grade
        return sum(self.__grades) / len(self.__grades)

    def display_info(self):
        super().display_info()  # display Person info first

        # display student-specific info
        print("Student ID:", self.__student_id)
        print("Course:", self.course)
        print("Average:", round(self.compute_average(), 2))


class WorkingStudent(Student):
    def __init__(self, name, age, student_id, course, grades, company_name):
        super().__init__(name, age, student_id, course, grades)  # inherit Student
        self.company_name = company_name  # store company name

    def display_info(self):
        super().display_info()  # display student info

        # display working student info
        print("Company:", self.company_name)


# ================= MAIN PROGRAM =================

students_list = []  # list to store all students
numStud = int(input("Enter number of students: "))  # number of entries

for i in range(numStud):
    print("\nStudent", i + 1)  # show student index

    # ---------------- NAME INPUT ----------------
    name = input("Enter name: ")

    # validate name (cannot be empty)
    while name.strip() == "":
        print("Name cannot be empty.")
        name = input("Enter name again: ")

    # ---------------- AGE INPUT ----------------
    age = input("Enter age: ")

    while True:
        try:
            age_int = int(age)  # convert input

            # check valid range
            if 1 <= age_int <= 100:
                age = age_int  # store valid age
                break  # exit loop
            else:
                print("Age must be 1-100")

        except:
            print("Age must be numeric")

        age = input("Enter age again: ")

    # ---------------- OTHER DETAILS ----------------
    student_id = input("Enter Student ID: ")
    course = input("Enter course: ")

    # ---------------- GRADES INPUT ----------------
    grades = []  # reset grade list per student

    print("Enter grades one by one (type 'done' to finish):")

    while True:
        g = input("Enter grade: ")

        if g.lower() == "done":
            break  # stop grade input

        try:
            g = float(g)  # convert grade

            # validate grade range
            if 0 <= g <= 100:
                grades.append(g)  # store grade
            else:
                print("Grade must be 0–100")

        except:
            print("Invalid input. Grade must be numeric.")

    # ---------------- STUDENT TYPE ----------------
    choice = input("Is working student? (y/n): ")

    if choice.lower() == "y":
        company = input("Enter company name: ")  # company input
        student = WorkingStudent(name, age, student_id, course, grades, company)
    else:
        student = Student(name, age, student_id, course, grades)

    students_list.append(student)  # store student object


# ================= DISPLAY ALL STUDENTS =================

print("\n===== ALL STUDENTS =====")

for s in students_list:
    s.display_info()  # show each student info
    print("------------------")


# ================= ANALYTICS =================

if len(students_list) > 0:

    total_avg = 0  # sum of all averages
    highest = students_list[0]  # initial highest
    lowest = students_list[0]   # initial lowest

    passed = []  # list of passing students
    failed = []  # list of failing students

    # loop through all students
    for s in students_list:
        avg = s.compute_average()  # get student average
        total_avg += avg  # add to total

        # check highest average
        if avg > highest.compute_average():
            highest = s

        # check lowest average
        if avg < lowest.compute_average():
            lowest = s

        # classify pass/fail
        if avg >= 75:
            passed.append(s)
        else:
            failed.append(s)

    # compute class average
    class_avg = total_avg / len(students_list)

    print("\n===== ANALYTICS SUMMARY =====")
    print("Class Average:", round(class_avg, 2))

    print("\nHighest Average Student:")
    highest.display_info()

    print("\nLowest Average Student:")
    lowest.display_info()

    print("\nPassed Students:")
    for s in passed:
        print(s.name)

    print("\nFailed Students:")
    for s in failed:
        print(s.name)

else:
    print("No students entered.")
