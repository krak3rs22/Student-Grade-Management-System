import smtplib

class Student:
    def __init__(self, email, name, surname, hmw1, hmw2, hmw3, hmw4, hmw5, test, exam, final=-1, status=None):
        self.email = email
        self.name = name
        self.surname = surname
        self.hmw1 = int(hmw1)
        self.hmw2 = int(hmw2)
        self.hmw3 = int(hmw3)
        self.hmw4 = int(hmw4)
        self.hmw5 = int(hmw5)
        self.test = int(test)
        self.exam = int(exam)
        self.final = float(final)
        self.status = status

    def calculate_final_grade(self):
        total_points = self.hmw1 + self.hmw2 + self.hmw3 + self.hmw4 + self.hmw5 + self.test + self.exam
        if total_points >= 91:
            self.final = 5
        elif 81 <= total_points <= 90:
            self.final = 4.5
        elif 71 <= total_points <= 80:
            self.final = 4
        elif 61 <= total_points <= 70:
            self.final = 3.5
        elif 51 <= total_points <= 60:
            self.final = 3
        else:
            self.final = 2

    def __repr__(self):
        return f"Student({self.email}, {self.name}, {self.surname}, {self.hmw1}, {self.hmw2}, {self.hmw3}, {self.hmw4}, {self.hmw5}, {self.test}, {self.exam}, {self.final}, {self.status})"

def load_students_data():
    students = {}
    with open("studenciZ3.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(",")
            email = data[0]
            name = data[1]
            surname = data[2]
            hmw1 = data[3]
            hmw2 = data[4]
            hmw3 = data[5]
            hmw4 = data[6]
            hmw5 = data[7]
            test = data[8]
            exam = data[9]
            final = data[10]
            status = data[11]
            student = Student(email, name, surname, hmw1, hmw2, hmw3, hmw4, hmw5, test, exam, final, status)
            students[email] = student
    return students

def save_students_data(students):
    with open("students.txt", "w") as file:
        for student in students.values():
            data = [str(student.email), str(student.name), str(student.surname), str(student.hmw1), str(student.hmw2),
                    str(student.hmw3), str(student.hmw4), str(student.hmw5), str(student.test),
                    str(student.exam), str(student.final), str(student.status)]
            line = ','.join(data) + '\n'
            print(data)
            print(line)
            file.write(line)

def add_student(students):
    email = input("Enter student's email: ")
    name = input("Enter student's name: ")
    surname = input("Enter student's surname: ")
    hmw1 = input("Enter student's hmw1 score: ")
    hmw2 = input("Enter student's hmw2 score: ")
    hmw3 = input("Enter student's hmw3 score: ")
    hmw4 = input("Enter student's hmw4 score: ")
    hmw5 = input("Enter student's hmw5 score: ")
    test = input("Enter student's test score: ")
    exam = input("Enter student's exam score: ")
    students[email] = Student(email, name, surname, hmw1, hmw2, hmw3, hmw4, hmw5, test, exam)
    save_students_data(students)

def remove_student(students):
    email = input("Enter email of the student to remove: ")
    if email in students:
        del students[email]
        save_students_data(students)
        print("Student removed successfully!")
    else:
        print("Student not found.")

def assign_grades(students):
    for student in students.values():
        if student.status not in ['GRADED', 'MAILED']:
            student.calculate_final_grade()
            student.status = 'GRADED'
    save_students_data(students)

def send_email(students):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your password: ")
    server.login(sender_email, sender_password)
    status = input("Enter status for the email: ")
    message = "Your grade has been posted!"
    for student in students.values():
        if student.status != 'MAILED':
            student.status = status
            email = student.email
            msg = f"Subject: Grade Notification\n\n{message}"
            server.sendmail(sender_email, email, msg)
            student.status = 'MAILED'
    server.quit()
    save_students_data(students)


