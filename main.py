class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def set_grade_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    # Calculating average score for students
    def calc_average_score_student(self):
        average_score = 0
        for grade, value in self.grades.items():
            try:
                average_score += sum(value)/len(value)
            except ZeroDivisionError:
                print("Division by zero error")
        try:
            return average_score / len(self.grades)
        except ZeroDivisionError:
            print("Division by zero error")

    def __str__(self):
        average_score = 0
        for grade, value in self.grades.items():
            average_score += sum(value)/len(value)
        print(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calc_average_score_student()}\n'
             f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')

    # The method of comparing students < by average grade
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calc_average_score_student() < other.calc_average_score_student()
        return False

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    # Calculating average score for lecturers
    def calc_average_score_lecturer(self):
        average_score = 0
        for grade, value in self.lecturer_grades.items():
            try:
                average_score += sum(value)/len(value)
            except ZeroDivisionError:
                print("Division by zero error")
        try:
            return average_score/len(self.lecturer_grades)
        except ZeroDivisionError:
            print("Division by zero error")

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calc_average_score_lecturer()}')

    # The method of comparing lecturers > by average grade
    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_average_score_lecturer() > other.calc_average_score_lecturer()
        return False


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')

def calculating_average_score_students(students, course):
    score_list = []
    for stud in students:
        if isinstance(stud, Student):
            average_score = 0
            for grade, value in stud.grades.items():
                if grade == course:
                    try:
                        average_score += sum(value) / len(value)
                    except ZeroDivisionError:
                        print("Division by zero error")
                    score_list.append(average_score)
                else:
                    continue
        else:
            continue
    if score_list:
        try:
            return round(sum(score_list) / len(score_list), 1)
        except ZeroDivisionError:
            print("Division by zero error")
    else:
        return "No students"

def calculating_average_score_lecturers(lecturers, course):
    score_list = []
    for lect in lecturers:
        if isinstance(lect, Lecturer) and course in lect.lecturer_grades:
            average_score = 0
            for grade, value in lect.lecturer_grades.items():
                if grade == course:
                    try:
                        average_score += sum(value) / len(value)
                    except ZeroDivisionError:
                        print("Division by zero error")
                    score_list.append(average_score)
                else:
                    continue
        else:
            continue
    if score_list:
        try:
            return round(sum(score_list) / len(score_list), 1)
        except ZeroDivisionError:
            print("Division by zero error")
    else:
        return "No students"

lecturer_1 = Lecturer('Peter', 'Petrovich')
lecturer_1.courses_attached = ['Python', 'C++']
some_reviewer = Reviewer('Some', 'Boody')
some_reviewer.courses_attached = ['Python', 'C++']
reviewer_1 = Reviewer('Masha', 'Boody')
reviewer_1.courses_attached = ['Python', 'C++']

lecturer_2 = Lecturer('Polina', 'Popova')
lecturer_2.courses_attached = ['Java', 'C++']

student_1 = Student('Olga', 'Pukh', 'w')
student_1.courses_in_progress = ['Python', 'C++']
student_1.finished_courses = ['Java', '1C']
some_reviewer.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 6)
some_reviewer.rate_hw(student_1, 'C++', 5)

student_2 = Student('Rita', 'Pukh', 'w')
student_2.courses_in_progress = ['Python', 'Java', 'C++']
student_2.finished_courses = ['SQL', '1C']
some_reviewer.rate_hw(student_2, 'Python', 5)

student_3 = Student('Olga', 'Pukh', 'w')
student_3.courses_in_progress = ['Python', 'C++']
student_3.finished_courses = ['SQL', '1C']
some_reviewer.rate_hw(student_3, 'Python', 1)

student_1.set_grade_lecturer(lecturer_1, 'Python', 9)
student_2.set_grade_lecturer(lecturer_1, 'Python', 7)
student_1.set_grade_lecturer(lecturer_1, 'C++', 4)
student_2.set_grade_lecturer(lecturer_1, 'C++', 7)

student_1.set_grade_lecturer(lecturer_2, 'Java', 8)
student_1.set_grade_lecturer(lecturer_2, 'C++', 9)
student_2.set_grade_lecturer(lecturer_2, 'Java', 10)
student_2.set_grade_lecturer(lecturer_2, 'C++', 8)

some_reviewer.__str__()
lecturer_1.__str__()
student_1.__str__()

print(student_2 < student_1)
print(student_1 < student_2)
print(lecturer_1 > lecturer_2)
print(lecturer_2 > lecturer_1)

students_list = []
students_list = [student_1, student_2, student_3]
lecturers_list = []
lecturers_list = [lecturer_1, lecturer_2]

print(calculating_average_score_students(students_list, 'Python'))
print(calculating_average_score_lecturers(lecturers_list, 'Python'))
print(calculating_average_score_lecturers(lecturers_list, 'SQL'))