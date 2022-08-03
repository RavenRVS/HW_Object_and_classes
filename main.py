from multiprocessing.sharedctypes import Value
import statistics;

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'
    
    def mean(self):
        grade_for_courses = [self.grades[key] for key in self.grades]
        all_grade = []
        for values in grade_for_courses:
            for value in values:
                all_grade.append(value)
        res_mean = statistics.mean(all_grade)
        return res_mean
    
    def __str__(self):
        string = (f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашнее задание: {round(self.mean(), 2)}
Курсы в процессе изучения: {str(self.courses_in_progress).strip('[]')}
Завершенные курсы: {str(self.finished_courses).strip('[]')}''')
        return string

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Студента можно сравнивать только со студентом')
            return
        return self.mean() < other.mean()    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  
      
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) 
        self.grades = {}

    def mean(self):
        grade_for_courses = [self.grades[key] for key in self.grades]
        all_grade = []
        for values in grade_for_courses:
            for value in values:
                all_grade.append(value)
        res_mean = statistics.mean(all_grade)
        return res_mean

    def __str__(self):
        string = (f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {round(self.mean(), 2)}''')
        return string

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лектора можно сравнивать только c лектором')
            return
        return self.mean() < other.mean()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 <= grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def __str__(self):
        string = (f'''Имя: {self.name}
Фамилия: {self.surname}''')
        return string

def av_grad_stud(students, course):
    mean_all_student = []
    for student in students:
        if isinstance(student, Student):
            if course in dict.keys(student.grades): 
                res_mean = statistics.mean(student.grades.get(course))
                mean_all_student.append(res_mean)
            else:
                continue            
        else:
            continue
    if len(mean_all_student) > 1:
        return round(statistics.mean(mean_all_student), 2)
    else:
        if len(mean_all_student) < 1:
            print('В списке нет студентов с оценками по данному курсу')
        else: 
            return mean_all_student[0]

def av_grad_lect(lecturers, course):
    mean_all_lecturer = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            if course in dict.keys(lecturer.grades): 
                res_mean = statistics.mean(lecturer.grades.get(course))
                mean_all_lecturer.append(res_mean)  
            else:
                continue       
        else:
            continue
    if len(mean_all_lecturer) > 1:
        return round(statistics.mean(mean_all_lecturer), 2)
    else:
        if len(mean_all_lecturer) < 1:
            print('В списке нет лекторов с оценками по данному курсу')
        else: 
            return mean_all_lecturer[0]

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['SQL']
best_student.finished_courses += ['Java']

best_of_the_best_student = Student('Chuck', 'Norris', 'MAN')
best_of_the_best_student.courses_in_progress += ['Python']
best_of_the_best_student.courses_in_progress += ['Java']
best_of_the_best_student.finished_courses += ['SQL']
 
cool_reviwer = Reviewer('Good', 'Boss')
cool_reviwer.courses_attached += ['Python']
cool_reviwer.courses_attached += ['SQL']

bad_reviwer = Reviewer('Bad', 'Boss')
bad_reviwer.courses_attached += ['Python']
bad_reviwer.courses_attached += ['Java']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']

cool_lecturer2 = Lecturer('Any', 'Buddy')
cool_lecturer2.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['SQL']

cool_reviwer.rate_hw(best_student, 'Python', 10)
cool_reviwer.rate_hw(best_student, 'Python', 8)
cool_reviwer.rate_hw(best_student, 'Python', 9)
cool_reviwer.rate_hw(best_student, 'SQL', 9)
cool_reviwer.rate_hw(best_student, 'SQL', 10)
cool_reviwer.rate_hw(best_student, 'SQL', 7)

bad_reviwer.rate_hw(best_of_the_best_student, 'Python', 10)
bad_reviwer.rate_hw(best_of_the_best_student, 'Python', 10)
bad_reviwer.rate_hw(best_of_the_best_student, 'Python', 9)
bad_reviwer.rate_hw(best_of_the_best_student, 'Java', 10)
bad_reviwer.rate_hw(best_of_the_best_student, 'Java', 10)
bad_reviwer.rate_hw(best_of_the_best_student, 'Java', 9)

best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer2, 'SQL', 10)
best_student.rate_hw(cool_lecturer2, 'SQL', 8)

best_of_the_best_student.rate_hw(cool_lecturer2, 'Python', 10)
best_of_the_best_student.rate_hw(cool_lecturer2, 'Python', 9)
best_of_the_best_student.rate_hw(cool_lecturer2, 'Python', 8)
best_of_the_best_student.rate_hw(cool_lecturer, 'Java', 9)
best_of_the_best_student.rate_hw(cool_lecturer, 'Java', 10)

Students = [best_of_the_best_student, best_student]
Lecturers = [cool_lecturer, cool_lecturer2]

print(cool_reviwer)
print(cool_lecturer)
print(best_student)

print(best_student < best_of_the_best_student)
print(cool_lecturer > cool_lecturer2)

print(av_grad_stud(Students, 'Python'))
print(av_grad_lect(Lecturers, 'Java'))
