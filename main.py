class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lect, course, grade):
        if isinstance(lect, Lecturer) and course in lect.courses_attached and course in self.courses_in_progress:
            if course in lect.grades_stud:
                lect.grades_stud[course] += [grade]
            else:
                lect.grades_stud[course] = [grade]
        else:
            return 'Ошибка'

    def middle_stud(self):
        rez = []
        for d in self.grades.values():
            rez += d
        return round(sum(rez) / len(self.grades), 2)

    def __str__(self):
        return f" Имя: {self.name}\n " \
               f"Фамилия: {self.surname}\n " \
               f"Средняя оценка за домашние задания: {self.middle_stud()}\n " \
               f"Курсы в процессе изучения: {self.courses_in_progress}\n " \
               f"Завершенные курсы: {self.finished_courses}"

    def __gt__(self, other_stud):
        if not isinstance(other_stud, Student):
            print('Это не студент')
            return
        return self.middle_stud() < other_stud.middle_stud()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    # ЛЕКТОРЫ
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_stud = {}

    def middle_grade(self):
        rez = []
        for d in self.grades_stud.values():
            rez += d
        return round(sum(rez) / len(self.grades_stud), 2)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.middle_grade()}'

    def __gt__(self, other_lect):
        if not isinstance(other_lect, Lecturer):
            print('Это не лектор')
            return
        return self.middle_grade() < other_lect.middle_grade()


class Reviewer(Mentor):
    # ЭКСПЕРТЫ ПРОВЕРЯЮЩИЕ
    # ============================================
    def rate_stud(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"


# ====================================================================================================

student_1 = Student('Ruoy', 'Eman', 'M')
student_1.courses_in_progress += ['Python', 'Git', 'DJANGO']

student_2 = Student('Jonn', 'Smith', 'M')
student_2.courses_in_progress += ['Python', 'Git', 'C++']

rev_1 = Reviewer('Some', 'Buddy')
rev_1.courses_attached += ['Python', 'Git', 'DJANGO']
rev_1.rate_stud(student_1, 'Python', 5)
rev_1.rate_stud(student_1, 'Git', 5.9)
rev_1.rate_stud(student_1, 'DJANGO', 3.8)


rev_1.rate_stud(student_2, 'Python', 10)
rev_1.rate_stud(student_2, 'C++', 3.9)
rev_1.rate_stud(student_2, 'Git', 7.5)

# print(Student.__str__(student_1))
# print(Student.__str__(student_2))
# print(student_2.grades)
# print(student_1 > student_2)

all_students = [student_1, student_2]


def Middle_all_students(students, courses):
    rez = []
    for d in students:
        for x, y in d.grades.items():
            if courses == x:
                rez.append(*y)
    print(sum(rez) / len(rez))


# Middle_all_students(all_students, 'C++')


def Middle_all_lectors(lectors, courses):
    rez = []
    for d in lectors:
        for x, y in d.grades.items():
            if courses == x:
                rez.append(*y)
    print(sum(rez) / len(rez))