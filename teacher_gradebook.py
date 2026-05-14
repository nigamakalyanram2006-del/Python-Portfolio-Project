#   ---teacher gradebook program---

class Student:
    def __init__(self, student_name):
        self.student_name = student_name
        self.student_grades = []

class Gradebook:
    def __init__(self):
        self.students = []

    def main_menu(self):
        while True:
            menu_options = int(input("Enter 1 to Add Student\nEnter 2 to Records Grades\nEnter 3 to View Student Info\nEnter 4 to View Full Class\nEnter 5 to Quit\n>>>"))
            if menu_options == 1:
                self.add_students()
            elif menu_options == 2:
                self.record_grades()
            elif menu_options == 3:
                self.view_student_info()
            elif menu_options == 4:
                self.view_full_class()
            elif menu_options == 5:
                break

    def add_students(self):
        add_student = input("Enter student name: ")
        new_student = Student(add_student)
        self.students.append(new_student)

    def record_grades(self):
        user_name = input("Enter student name: ")
        user_grade = float(input("Enter student grade: "))
        for name in self.students:
            if name.student_name == user_name:
                name.student_grades.append(user_grade)


    def view_student_info(self):
        user_name = input("Enter student name: ")
        for name in self.students:
            if name.student_name == user_name:
                print(f"Student Name: {name.student_name}\nStudent Grades: {name.student_grades}")

    def view_full_class(self):
        for name in self.students:
            print(f"Student Name: {name.student_name}\nStudent Grades: {name.student_grades}")

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip().split(",")
                new_student = Student(line[0])
                for grade in line[1:]:
                    new_student.student_grades.append(float(grade))
                self.students.append(new_student)
                

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for name in self.students:
                grades = []
                for grade in name.student_grades:
                    grades.append(str(grade))
                student_grades = ",".join(grades)
                file.write(name.student_name + "," + student_grades + "\n")
            


the_file = Gradebook()
the_file.load_from_file("teacher_gradebook.txt")
the_file.main_menu()
the_file.save_to_file("teacher_gradebook.txt")