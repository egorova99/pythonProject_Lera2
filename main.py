class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_average = {}

    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.lector_grades:
                lector.lector_grades[course] += [grade]
            else:
                lector.lector_grades[course] = [grade]
        else:
            return 'Mistake'

        list = []
        for value in lector.lector_grades.values():
            for ing in value:
                list.append(ing)
        lector.lector_grades_average = sum(list) / len(list)

    def __lt__(self, other):
        self.a = self.grades_average
        other.a = other.grades_average
        if self.a < other.a:
            print(f'Наивысший средний бал ' + str(other.a) + ' у студента ' + other.name)
            return (other.a)
        else:
            print(f'Наивысший средний бал ' + str(self.a) + ' у студента ' + self.name)
            return (self.a)

    def __str__(self):
        return (
                    '\nprint(some_student)\nИмя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за домашние задания: ' + str(
                self.grades_average) + '\nКурсы в процессе изучения: ' + str(self.courses_in_progress).strip(
                '[]') + '\nЗавершенные курсы: ' + str(self.finished_courses).strip('[]') + '\n')

    def course_lec_rate(self, lectors, course):
        course_grades = {}
        # print(students)
        for lec in lectors:
            for k, v in lec.lector_grades.items():
                if k == course:
                    course_grades[lec.name] = v
        course_grades2 = []
        for k, v in course_grades.items():
            course_grades2 = course_grades2 + v
            course_grades_average = sum(course_grades2) / len(course_grades2)
        print(f'Cредняя оценка всех лекторов в рамках курса {course}: {course_grades_average}')

    def __str__(self):
        return ('\nprint(some_reviewer)\nИмя: ' + self.name + '\nФамилия: ' + self.surname)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.course_grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_grades = {}
        self.lector_grades_average = {}

    def __lt__(self, other):
        self.a = self.lector_grades_average
        other.a = other.lector_grades_average
        if self.a < other.a:
            print(f'\nНаивысший средний бал ' + str(other.a) + ' у лектора ' + other.name)
            return (other.a)
        else:
            print(f'\nНаивысший средний бал ' + str(self.a) + ' у лектора ' + self.name)
            return (self.a)

    def __str__(self):
        return (
                    '\nprint(some_lecturer)\nИмя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' + str(
                self.lector_grades_average))


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Mistake'

        list = []
        for value in student.grades.values():
            for ing in value:
                list.append(ing)
        student.grades_average = sum(list) / len(list)

    def course_hw_rate(self, students, course):
        course_grades = {}
        # print(students)
        for st in students:
            for k, v in st.grades.items():
                if k == course:
                    course_grades[st.name] = v
            #   print(f'%%%%%{course}%%{course_grades}')
            # else:
            #   print(f'@@@@@{course}@@{course_grades}')
        course_grades2 = []
        for k, v in course_grades.items():
            course_grades2 = course_grades2 + v
            course_grades_average = sum(course_grades2) / len(course_grades2)
            # print(course_grades2)
        print(f'Cредняя оценка за дз всех студентов в рамках курса {course}: {course_grades_average}')

    def __str__(self):
        return ('\nprint(some_reviewer)\nИмя: ' + self.name + '\nФамилия: ' + self.surname)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.grades['Git'] = [10, 9]
best_student.grades['Python'] = [8]
# print(f'студент_курсы в процессе прохождения {best_student.courses_in_progress}')
# print(f'best_student.finished_courses {best_student.finished_courses}')
# print(f'best_student.grades {best_student.grades}')

best_student2 = Student('Jay', 'Lo', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.grades['Python'] = [5, 8]
# best_student2.grades['Git'] = [5, 8]

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(f'cool_mentor.courses_attached {cool_mentor.courses_attached}')


# Задание № 1 Наследование классов Reviewer (эксперты, проверяющие домашние задания).
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
print(f'эксперт по дз {some_reviewer.name} закрепленные курсы {some_reviewer.courses_attached}')

some_reviewer2 = Reviewer('Ray', 'Ban')
some_reviewer2.courses_attached += ['Python']
print(f'эксперт по дз {some_reviewer2.name} закрепленные курсы {some_reviewer2.courses_attached}')

# Задание № 2 выставлять студентам оценки за домашние задания
some_reviewer.rate_hw(best_student, 'Python', 4)
some_reviewer.rate_hw(best_student, 'Git', 5)
some_reviewer.rate_hw(best_student, 'Git', 6)
some_reviewer.rate_hw(best_student2, 'Python', 10)
some_reviewer.rate_hw(best_student2, 'Python', 9)
print(f'оценки студенту {best_student.name} за домашние задания {best_student.grades}')
print(f'оценки студенту {best_student2.name} за домашние задания {best_student2.grades}')
# print(Reviewer.mro())

# Задание № 1 Наследование классов Lecturer (лекторы)
some_lector = Lecturer('Some', 'Buddy')
some_lector.courses_attached += ['Python']
print(f'лектор {some_lector.name} закрепленные курсы {some_lector.courses_attached}')
some_lector2 = Lecturer('Ray', 'Ban')
some_lector2.courses_attached += ['Python']
print(f'лектор {some_lector2.name} закрепленные курсы {some_lector2.courses_attached}\n')
# some_lector2.lector_grades['Python'] = [8, 9, 10]
some_lector.courses_attached += ['Git']
# some_lector.lector_grades['Git'] = [1, 2, 7]
# some_lector.lector_grades['Python'] = [3]
# print(f'оценки лектора {some_lector.lector_grades}')
# print(Lecturer.mro())

# Задание № 2 выставлять лекторам оценки за лекции от студентов
some_lecture = Student('Ruoy', 'Eman', 'your_gender')
some_lecture.courses_in_progress += ['Python']
some_lecture.courses_in_progress += ['Git']
some_lecture.rate_lecture(some_lector, 'Python', 5)
some_lecture.rate_lecture(some_lector, 'Python', 6)
some_lecture.rate_lecture(some_lector, 'Python', 7)
some_lecture.rate_lecture(some_lector, 'Git', 8)
some_lecture.rate_lecture(some_lector2, 'Python', 9)
some_lecture.rate_lecture(some_lector2, 'Python', 10)

print(f'оценки лектору {some_lector.name} {some_lector.lector_grades}')
print(f'оценки лектору {some_lector2.name} {some_lector2.lector_grades}')

# Задание № 3.1 Перегрузите магический метод __str__ у всех классов.
print(some_reviewer)
print(some_lector)
print(some_lector2)
print(best_student)
print(best_student2)

# Задание № 3.2 Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
is_lt = (some_lector < some_lector2)
is_lt = (best_student < best_student2)

# Задание № 4.1 реализуйте функции: для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
some_reviewer.course_hw_rate([best_student, best_student2], 'Python')
some_reviewer.course_hw_rate([best_student, best_student2], 'Git')

# Задание № 4.2 реализуйте функции: для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).
some_lecture.course_lec_rate([some_lector, some_lector2], 'Python')
some_lecture.course_lec_rate([some_lector, some_lector2], 'Git')