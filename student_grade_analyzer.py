class Student:
    def __init__(self, name):
        self.student_name = name
        self.subject_and_grades = {}

    def __str__(self):
        grades_str = ""
        for key, value in self.subject_and_grades.items():
            grades_str = grades_str + f"{key}: {value}  "
        return f"Student: {self.student_name}\nGrades: {grades_str}"
    
    def add_grade(self, subject, grade):
        self.subject_and_grades[subject] = grade
        
    def get_average(self):
        if len(self.subject_and_grades) == 0:
            return 0
        average = 0
        for key, value in self.subject_and_grades.items():
            average = average + value
        average = average / len(self.subject_and_grades)
        average = int(average)
        return average

class GradeAnalyzer:
    def __init__(self):
        self.student_objects = []
        self.filename = "student_data.txt"
        self.reportfile = "report.txt"
        self.load_from_file()

    def main_menu(self):
        while True:
            menu_options = int(input("Enter 1 to Add Student\nEnter 2 to Add grade to Student\nEnter 3 to Generate Report\nEnter 4 to show highest performer\nEnter 5 to show lowest performer\nEnter 6 to Quit\n>>>"))
            if menu_options == 1:
                name = input("Enter Student Name: ")
                self.add_student(name)
            elif menu_options == 2:
                name = input("Enter Student Name: ")
                subject = input("Enter Subject: ")
                grade = int(input("Enter Grade: "))
                self.add_grade_to_student(name, subject, grade)
            elif menu_options == 3:
                self.generate_report()
            elif menu_options == 4:
                print(self.get_highest_performer())
            elif menu_options == 5:
                print(self.get_lowest_performer())
            elif menu_options == 6:
                break

    def add_student(self, name):
        student = Student(name)
        self.student_objects.append(student)

    def add_grade_to_student(self, name, subject, grade):
        for student in self.student_objects:
            if student.student_name == name:
                student.add_grade(subject, grade)
        self.save_to_file()

    def get_highest_performer(self):
        best_student = None
        best_average = 0
        for student in self.student_objects:
            if student.get_average() > best_average:
                best_average = student.get_average()
                best_student = student.student_name
        return best_student
    
    def get_lowest_performer(self):
        worst_student = None
        worst_average = 999
        for student in self.student_objects:
            if student.get_average() < worst_average:
                worst_average = student.get_average()
                worst_student = student.student_name
        return worst_student
    
    def generate_report(self):
        with open(self.reportfile, "w") as file:
            file.write("---Student Grade Analyzer Report---\n")
            for student in self.student_objects:
                file.write("Student: " + student.student_name + "\n")
                file.write("Grades: " + str(student.subject_and_grades) + "\n")
                file.write("Average: " + str(student.get_average()) + "\n")
                file.write("---\n") 
            file.write("Highest Performer: " + self.get_highest_performer() + "\n")
            file.write("Lowest Performer: " + self.get_lowest_performer() + "\n")

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for student in self.student_objects:
                grades_line = ""
                for subject, grade in student.subject_and_grades.items():
                    grades_line = grades_line + subject + ":" + str(grade) + "|"
                file.write(student.student_name + "|" + grades_line + "\n")

    def load_from_file(self):
        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip().split("|")
                student = Student(line[0])
                self.student_objects.append(student)
                for item in line[1:]:
                    subject, grade = item.split(":")
                    student.add_grade(subject, grade)
                

analyzer = GradeAnalyzer()
analyzer.main_menu()