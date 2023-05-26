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
    
    def rate_webin(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def feedback(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades] # Список со всеми оценками
        total_grades = sum(all_grades) # Сумма всех оценок
        count = len(all_grades) # Количество всех оценок
        avg_grade = total_grades / count # Считаю среднею оценку
        return avg_grade
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.feedback()}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Этот человек не обучается!')
            return
        return self.feedback() < other.feedback()
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def feedback(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades] # Список со всеми оценками
        total_grades = sum(sum(grades) for grades in self.grades.values()) # Сумма всех оценок
        count = len(all_grades) # Количество всех оценок
        avg_grade = total_grades / count # Считаю среднею оценку
        return avg_grade
    # Пожалуйста помогите мне понять как можно сделать этот подсчет без генератора и сумм в сумме (если это возможно)
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.feedback()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Этот человек не обучает!')
            return
        return self.feedback() < other.feedback()


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
        str = f'Имя: {self.name}\nФамилия: {self.surname}'
        return str

 
student = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Abegru', 'Aldruv', 'your_gender')

student.courses_in_progress += ['Python']
student2.courses_in_progress += ['Python']

student.add_courses('Введение в программирование')
student2.add_courses('Введение в программирование')

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']
reviewer2 = Reviewer('Any', 'Bodie')
reviewer2.courses_attached += ['Python']
 
reviewer.rate_hw(student, 'Python', 9)
reviewer2.rate_hw(student, 'Python', 7)
reviewer.rate_hw(student, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 6)

lecturer = Lecturer('Hobot', 'One')
lecturer2 = Lecturer('Human', 'Being')

lecturer.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']

student.rate_webin(lecturer, 'Python', 10)
student2.rate_webin(lecturer, 'Python', 6)
student.rate_webin(lecturer2, 'Python', 7)
student2.rate_webin(lecturer2, 'Python', 4)
student.rate_webin(lecturer, 'Python', 8)
student2.rate_webin(lecturer, 'Python', 7)
student.rate_webin(lecturer2, 'Python', 9)
student2.rate_webin(lecturer2, 'Python', 8)

print(f'{student}\n\n{student2}\n\n{reviewer}\n\n{reviewer2}\n\n{lecturer}\n\n{lecturer2}')

def all_stud_avg(list_stud, course):
    def specialized_feedback(stud, course):
        all_grades = [grades for grades in stud.grades[course]]
        total_grades = sum(all_grades)
        count = len(all_grades)
        avg_grade = total_grades / count
        return avg_grade
    
    stud_count = len(list_stud) # количество учащихся
    total_grades = 0
    
    for stud in list_stud:
        total_grades += specialized_feedback(stud, course)
    
    return total_grades / stud_count


def all_lect_avg(list_lect, course):
    def specialized_feedback(lect, course):
        all_grades = [grades for grades in lect.grades[course]]
        total_grades = sum(all_grades)
        count = len(all_grades)
        avg_grade = total_grades / count
        return avg_grade
    
    lect_count = len(list_lect) # количество учащих
    total_grades = 0
    
    for stud in list_lect:
        total_grades += specialized_feedback(stud, course)
    
    return total_grades / lect_count


print(' ')
print("Функция для студентов: ",all_stud_avg([student, student2], 'Python'))
print(' ')
print("Функция для лекторов: ",all_lect_avg([lecturer, lecturer2], 'Python'))