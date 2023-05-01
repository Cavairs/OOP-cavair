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
       
    # def rate_hw(self, student, course, grade):
    #     """Студенты могут выставлять оценки лекторам """
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка' 
    # 

    def Lector_grade(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_attached:
            lector.grades[course] += [grade]       
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
        
class Lecturer (Mentor):
    pass

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Выставлять оценки студентам могут только ревьювервы"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 

best_student = Student('Ruoy', 'Eman', 'your_gender')
 
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 15)

# cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)