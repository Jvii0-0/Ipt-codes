class Person:
    def __init__(self, name, age):

        # Check if name is empty
        if name.strip() == "":
            print("Invalid name")
            self.name = "Unknown"  # default value if invalid
        else:
            self.name = name  # assign valid name

        # Validate age input
        try:
            age = int(age)  # convert age to integer

            # check if age is within valid range
            if age >= 1 and age <= 100:
                self.age = age
            else:
                print("Age must be between 1 and 100")
                self.age = 0  # default invalid value

        except:
            print("Age must be numeric")
            self.age = 0  # fallback if conversion fails

    def display_info(self):
        # display basic person information
        print("Name:", self.name)
        print("Age:", self.age)


# ================= STUDENT CLASS =================

class Student(Person):
    def __init__(self, name, age, student_id, course, grades):
        super().__init__(name, age)  # inherit Person attributes

        self.__student_id = student_id  # private student ID
        self.__grades = []  # list to store grades
        self.course = course  # course name

        # loop through all input grades
        for grade in grades:
            try:
                grade = float(grade)  # convert grade to float

                # validate grade range
                if grade >= 0 and grade <= 100:
                    self.__grades.append(grade)  # store valid grade
                else:
                    print("Invalid grade:", grade)

            except:
                print("Invalid grade:", grade)


    def compute_grade(self):
        # return 0 if no grades exist
        if len(self.__grades) == 0:
            return 0

        # compute average grade
        return sum(self.__grades) / len(self.__grades)


    def display_info(self):
        super().display_info()  # show Person info first

        # display student details
        print("Student ID:", self.__student_id)
        print("Course:", self.course)
        print("Average:", round(self.compute_grade(), 2))


# ================= WORKING STUDENT =================

class WorkingStudent(Student):
    def __init__(self, name, age, student_id, course, grades, company):
        super().__init__(name, age, student_id, course, grades)  # inherit Student
        self.company_name = company  # store company name

    def display_info(self):
        super().display_info()  # show student info
        print("Company Name:", self.company_name)  # show company


# ================= MAIN PROGRAM =================

students_list = []  # list to store all students
Snum = int(input("Enter number of students: "))  # number of students

for i in range(Snum):
    print("\nStudent", i + 1)  # show student index

    # ---------------- NAME INPUT VALIDATION ----------------
    name = input("Enter student name: ")

    # check if name is empty or contains numbers
    while name.strip() == "" or any(char.isdigit() for char in name):
        print("Name cannot be empty or contain numbers")
        name = input("Enter name again: ")

    # ---------------- AGE INPUT VALIDATION ----------------
    age = input("Enter age: ")

    while True:
        try:
            age_int = int(age)  # convert input to int

            # check valid age range
            if age_int >= 1 and age_int <= 100:
                age = age_int
                break  # exit loop if valid
            else:
                print("Age must be 1 - 100")

        except:
            print("Age must be numeric")

        age = input("Enter age again: ")

    # ---------------- OTHER DETAILS ----------------
    student_id = input("Enter student ID: ")
    course = input("Enter course: ")

    # ---------------- GRADES INPUT ----------------
    grades = []  # reset grades per student
    print("Enter grades (type 'done' to finish)")

    while True:
        grade = input("Enter grade: ")

        if grade.lower() == "done":
            break  # stop input

        try:
            g = float(grade)  # convert to float

            # validate grade range
            if g >= 0 and g <= 100:
                grades.append(g)  # store valid grade
            else:
                print("Grade must be 0 - 100")

        except:
            print("Invalid grade")

    # ---------------- CHECK STUDENT TYPE ----------------
    choice = input("Are you a working student? (y/n): ")

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
    print("------------------")  # separator
