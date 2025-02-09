class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if course in lecturer.courses_attached and (course in self.finished_courses or course in
                                                     self.courses_in_progress):
            lecturer.lecturer_grades.setdefault(course, [])
            lecturer.lecturer_grades[course] += [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                f'{counting(self.grades)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__ (self, name, surname):
        Mentor.__init__(self, name, surname)
        self.lecturer_grades = {}

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:"
                f" {counting(self.lecturer_grades)}")

class Reviewer(Mentor):
    def __init__ (self, name, surname):
        Mentor.__init__(self, name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses
            and isinstance(self, Reviewer)):
            student.grades.setdefault(course, [])
            student.grades[course] += [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def counting(dictionary):
    sum_grades = 0
    len_grades = 0
    for sgrades in dictionary.values():
        sum_grades += sum(sgrades)
        len_grades += len(sgrades)
        return round(sum_grades/len_grades, 2)

def counting_student(student1, student2,comparison):
    if comparison == ">":
       return counting(student1.grades) > counting(student2.grades)
    elif comparison == "<":
        return counting(student1.grades) < counting(student2.grades)
    elif comparison == "=":
        return counting(student1.grades) == counting(student2.grades)
    else:
        print("недопустимый знак")

def counting_lecturer(lecturer1, lecturer2, comparison):
    if comparison == ">":
        return counting(lecturer1.lecturer_grades) > counting(lecturer2.lecturer_grades)
    elif comparison == "<":
        return counting(lecturer1.lecturer_grades) < counting(lecturer2.lecturer_grades)
    elif comparison == "=":
        return counting(lecturer1.lecturer_grades) == counting(lecturer2.lecturer_grades)
    else:
        print("недопустимый знак")

def counting_cours_stud(students, course):
    sum_grades = 0
    len_grades = 0
    for student in students:
        if course in student.grades:
            sum_grades += sum(student.grades[course])
            len_grades += len(student.grades[course])
    return round(sum_grades/len_grades, 2)

def counting_cours_lect(lectors, course):
    sum_grades = 0
    len_grades = 0
    for lector in lectors:
        if course in lector.lecturer_grades:
            sum_grades += sum(lector.lecturer_grades[course])
            len_grades += len(lector.lecturer_grades[course])
    return round(sum_grades/len_grades, 2)

student1 = Student('Roman', 'Petrov','Man')
student1.finished_courses = ['python', 'java']
student1.courses_in_progress = ['c++']
student2 = Student('Ira', 'Semenova', 'Women')
student2.finished_courses = ['c++', 'python']
student2.courses_in_progress = ['java']
lector1 = Lecturer('Ivan', 'Ivanov')
lector1.courses_attached = ['python', 'java']
lector2 = Lecturer ('Vlad', 'Polish')
lector2.courses_attached = ['c++']
reviewer1 = Reviewer('Igor', 'Sidorov')
reviewer1.courses_attached = ['python', 'java']
reviewer2 = Reviewer('Denis', 'Korobov')
reviewer2.courses_attached = ['c++']



Student.rate_lect(student1,lector1,'java', 8)
Student.rate_lect(student1,lector1,'python', 5)
Student.rate_lect(student2,lector2,'c++', 7)
Student.rate_lect(student2,lector1,'python', 6)

Reviewer.rate_hw(reviewer1, student1, 'python', 9)
Reviewer.rate_hw(reviewer1, student1, 'java', 10)
Reviewer.rate_hw(reviewer1, student2, 'python', 9)
Reviewer.rate_hw(reviewer2, student2, 'c++', 8)

print(f'{reviewer1.__str__()}\n{reviewer2.__str__()}')
print(f'{lector1.__str__()}\n{lector2.__str__()}')
print(f'{student1.__str__()}\n{student2.__str__()}')
print(f"student1 лучше student2: {counting_student(student1,student2,'>')}")
print(f"lector1 равен lector2: {counting_lecturer(lector1,lector2,'=')}")
print(counting_cours_stud([student1, student2], 'python'))
print(counting_cours_lect([lector1, lector2], 'python'))