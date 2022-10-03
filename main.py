class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress\
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        sum_ = 0
        count = 0
        for grades in self.grades.values():
            sum_ += sum(grades)
            count += len(grades)
        if count == 0:
            return 'Нет оценок'
        return sum_ / count

    def __str__(self):
        student = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self._average_grade():.2f}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
        '''
        return student

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self._average_grade() < other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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
        reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return reviewer


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        sum_ = 0
        count = 0
        for grades in self.grades.values():
            sum_ += sum(grades)
            count += len(grades)
        if count == 0:
            return 'Нет оценок'
        return sum_ / count

    def __str__(self):
        lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade():.2f}'
        return lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self._average_grade() < other._average_grade()


def avg_hw_grade(students, course):
    sum_ = 0
    count = 0
    for grades in students:
        for course_name, course_grades in grades.items():
            if course_name == course:
                sum_ += sum(course_grades)
                count += len(course_grades)
    if count == 0:
        return 'Ошибка'
    return sum_ / count


def avg_lectures_grade(lecturers, course):
    sum_ = 0
    count = 0
    for grades in lecturers:
        for course_name, course_grades in grades.items():
            if course_name == course:
                sum_ += sum(course_grades)
                count += len(course_grades)
    if count == 0:
        return 'Ошибка'
    return sum_ / count


first_student = Student('Ruoy', 'Eman', 'female')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses.append('Java')

second_student = Student('John', 'Wick', 'male')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses.append('C++')

first_reviewer = Reviewer('Ivan', 'Ivanov')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']

second_reviewer = Reviewer('Oleg', 'Smirnov')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 7)

first_reviewer.rate_hw(first_student, 'Git', 7)
first_reviewer.rate_hw(first_student, 'Git', 7)
first_reviewer.rate_hw(first_student, 'Git', 7)

first_reviewer.rate_hw(second_student, 'Python', 8)
first_reviewer.rate_hw(second_student, 'Python', 6)
first_reviewer.rate_hw(second_student, 'Python', 9)

first_reviewer.rate_hw(second_student, 'Git', 9)
first_reviewer.rate_hw(second_student, 'Git', 7)
first_reviewer.rate_hw(second_student, 'Git', 10)

second_reviewer.rate_hw(first_student, 'Python', 5)
second_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'Python', 6)

second_reviewer.rate_hw(first_student, 'Git', 5)
second_reviewer.rate_hw(first_student, 'Git', 4)
second_reviewer.rate_hw(first_student, 'Git', 3)

second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 10)

second_reviewer.rate_hw(second_student, 'Git', 5)
second_reviewer.rate_hw(second_student, 'Git', 4)
second_reviewer.rate_hw(second_student, 'Git', 8)

first_lecturer = Lecturer('Misha', 'Sobolev')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']

second_lecturer = Lecturer('Petya', 'Frolov')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

first_student.rate_lecture(first_lecturer, 'Python', 1)
first_student.rate_lecture(first_lecturer, 'Python', 2)
first_student.rate_lecture(first_lecturer, 'Python', 3)

first_student.rate_lecture(first_lecturer, 'Git', 3)
first_student.rate_lecture(first_lecturer, 'Git', 2)
first_student.rate_lecture(first_lecturer, 'Git', 1)

first_student.rate_lecture(second_lecturer, 'Python', 5)
first_student.rate_lecture(second_lecturer, 'Python', 5)
first_student.rate_lecture(second_lecturer, 'Python', 5)

first_student.rate_lecture(second_lecturer, 'Git', 5)
first_student.rate_lecture(second_lecturer, 'Git', 4)
first_student.rate_lecture(second_lecturer, 'Git', 5)



print(first_student)
print(second_student)
print(first_reviewer)
print(second_reviewer)
print(first_lecturer)
print(second_lecturer)
print(second_lecturer < first_lecturer)
print(second_student > first_student)

students = [first_student.grades, second_student.grades]

course = input('Введите название курса для средней оценки за ДЗ: ').capitalize()
if course not in first_student.courses_in_progress and course not in second_student.courses_in_progress:
    print('Ни один студент не проходит введеный вами курс')
else:
    print(f'Средняя оценка по курсу {course} за ДЗ: {avg_hw_grade(students, course):.2f}')

lecturers = [first_lecturer.grades, second_lecturer.grades]

course = input('Введите название курса для средней оценки за лекции: ').capitalize()
if course not in first_lecturer.courses_attached and course not in second_lecturer.courses_attached:
    print('Ни один лектор не преподает введеный вами курс')
else:
    print(f'Средняя оценка по курсу {course} за лекции: {avg_lectures_grade(lecturers, course):.2f}')