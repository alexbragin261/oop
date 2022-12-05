class Student:
    students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        super().__init__()
        Student.students.append(self)

    def __del__(self):
        Student.students.remove(self)

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _calc_average(self):
        average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 2)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {self._calc_average()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self._calc_average() < other._calc_average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturers.append(self)

    def __del__(self):
        Lecturer.lecturers.remove(self)

    def _calc_average(self):
        average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 2)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._calc_average()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self._calc_average() < other._calc_average()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.courses_in_progress += ['Rust']
student_1.finished_courses += ['Git']
student_1.finished_courses += ['C++']
student_2 = Student('Eva', 'Adams', 'female')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Git']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Java', 9)
reviewer_2 = Reviewer('Barak', 'Obama')
reviewer_2.courses_attached += ['Python']

lecturer_1 = Lecturer('Leo', 'Messi')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_2 = Lecturer('Elon', 'Musk')
lecturer_2.courses_attached += ['Python']

student_1.rate_lecturers(lecturer_1, 'Python', 10)
student_1.rate_lecturers(lecturer_1, 'Java', 9)
student_1.rate_lecturers(lecturer_1, 'Java', 7)
student_2.rate_lecturers(lecturer_1, 'Python', 5)
student_2.rate_lecturers(lecturer_2, 'Python', 4)
student_2.rate_lecturers(lecturer_1, 'Java', 3)
student_2.rate_lecturers(lecturer_2, 'Python', 3)

students = Student.students
lecturers = Lecturer.lecturers


def count_students(study, courses):
    # courses = input('Введите название курса ')
    rating_list = []
    for i in study:
        if courses in i.grades.keys():
            rating_list += i.grades.get(courses)
    return round(sum(rating_list) / len(rating_list), 2)


print(count_students(students, 'Java'))


def count_lecturers(teachers, courses):
    # courses = input('Введите название курса ')
    rating_list = []
    for i in teachers:
        if courses in i.grades.keys():
            rating_list += i.grades.get(courses)
    return round(sum(rating_list) / len(rating_list), 2)


print(count_lecturers(lecturers, 'Python'))
