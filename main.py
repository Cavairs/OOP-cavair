class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Student(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and grade in range(1, 11):
            if course in lector.rating:
                lector.rating[course].append(grade)
            else:
                lector.rating[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self, course):
        if course not in self.grades:
            return 'Нет оценок по данному курсу'
        else:
            return round(sum(self.grades[course])/len(self.grades[course]), 2)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade('Python')}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def avg_lecture_grade(self):
        if not self.rating:
            return None
        sum_grade = 0
        count = 0
        for grades in self.rating.values():
            for grade in grades:
                sum_grade += grade
                count += 1
        return round(sum_grade / count, 2)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_lecture_grade()}\n"

    def __lt__(self, other):
        return self.avg_lecture_grade() < other.avg_lecture_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and grade in range(1, 11):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


# создаем тестовых студентов, лекторов и экспертов
student_1 = Student('Юрий', 'Петров', 'm')
student_1.courses_in_progress += ['Python']
student_1.courses_attached += ['Python']
student_2 = Student('Игорь', 'Колесников', 'm')
student_2.courses_in_progress += ['Python']
student_2.courses_attached += ['Python']

lecturer_1 = Lecturer('Вадим', 'Товкало')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Даниил', 'Белобров')
lecturer_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Алиса', 'Ежеля')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Наталья', 'Балакина')
reviewer_2.courses_attached += ['Python']

# добавляем оценки студентам у лекторов, проверяем среднюю оценку у лекторов
student_1.rate_lector(lecturer_1, 'Python', 10)
student_1.rate_lector(lecturer_2, 'Python', 9)
student_2.rate_lector(lecturer_1, 'Python', 8)
student_2.rate_lector(lecturer_2, 'Python', 7)
print(lecturer_1)
print(lecturer_2)

# добавляем оценки студентам у проверяющих
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)


print(f"===Ревьювер===: \n{reviewer_1}\n\n===Лектор===:\n{lecturer_1}\n\n===Студент===:\n{student_1}")