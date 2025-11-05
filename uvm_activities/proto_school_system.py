class Person:
    counter = 0

    def __init__(self, first_name, last_name, gender, age):
        Person.counter += 1
        self.id = Person.counter
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def display_data(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")


class Professor(Person):
    prof_counter = 0

    def __init__(self, first_name, last_name, gender, age, degree, license):
        super().__init__(first_name, last_name, gender, age)
        Professor.prof_counter += 1
        self.id = Professor.prof_counter
        self.degree = degree
        self.license = license

    def display_data(self):
        super().display_data()
        print(f"Degree: {self.degree}")
        print(f"License: {self.license}")
        print("------------------------")


class Subject:
    subject_counter = 0

    def __init__(self, name, credits, professor):
        Subject.subject_counter += 1
        self.id = Subject.subject_counter
        self.name = name
        self.credits = credits
        self.professor = professor

    def display_data(self):
        print(f"ID: {self.id}")
        print(f"Subject Name: {self.name}")
        print(f"Credit Count: {self.credits}")
        print("------------------------")


class Student(Person):
    student_counter = 0

    def __init__(self, first_name, last_name, control_number, age, gender, semester):
        super().__init__(first_name, last_name, gender, age)
        Student.student_counter += 1
        self.id = Student.student_counter
        self.control_number = control_number
        self.semester = semester
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def display_data(self):
        super().display_data()
        print(f"Control Number: {self.control_number}")
        print(f"Semester: {self.semester}")
        print(f"Subjects Enrolled: {len(self.subjects)}")
        print("------------------------")


class System:
    def __init__(self):
        self.professors = []
        self.subjects = []
        self.students = []

    def register_professor(self):
        first_name = input("Enter professor's first name: ")
        last_name = input("Enter professor's last name: ")
        gender = input("Enter gender: ")
        age = int(input("Enter age: "))
        degree = input("Enter degree or profession: ")
        license = input("Enter professional license: ")
        self.professors.append(Professor(first_name, last_name, gender, age, degree, license))

    def register_subject(self):
        if not self.professors:
            print("No professors registered.")
            return
        name = input("Enter subject name: ")
        credits = int(input("Enter number of credits: "))
        self.subjects.append(Subject(name, credits, self.professors[0]))

    def register_student(self):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        control_number = int(input("Enter control number: "))
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        semester = int(input("Enter semester: "))
        student = Student(first_name, last_name, control_number, age, gender, semester)

        for subject in self.subjects:
            option = input(f"Add subject {subject.id} ({subject.name})? (y/n): ").lower()
            if option == 'y':
                student.add_subject(subject)

        self.students.append(student)

    def show_professor(self, id):
        for prof in self.professors:
            if prof.id == id:
                prof.display_data()
                return
        print("Professor not found.")

    def show_subject(self, id):
        for subj in self.subjects:
            if subj.id == id:
                subj.display_data()
                return
        print("Subject not found.")

    def show_student(self, id):
        for stu in self.students:
            if stu.id == id:
                stu.display_data()
                return
        print("Student not found.")


def main():
    system = System()

    for i in range(3):
        print(f"\nRegistering professor {i + 1}")
        system.register_professor()

    for i in range(4):
        print(f"\nRegistering subject {i + 1}")
        system.register_subject()

    for i in range(3):
        print(f"\nRegistering student {i + 1}")
        system.register_student()

    while True:
        print("\nView:\n1. Professor\n2. Subject\n3. Student\n4. Exit")
        option = input("Option: ")
        if option == '4':
            print("Exiting system...")
            break
        id = int(input("Enter ID: "))
        if option == '1':
            system.show_professor(id)
        elif option == '2':
            system.show_subject(id)
        elif option == '3':
            system.show_student(id)
        else:
            print("Invalid option.")

main()