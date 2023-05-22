class Student:

    def __init__(self, name, surname, course, marks):
        self.name = name
        self.surname = surname
        self.course = course
        self.marks = marks

    def get_info(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Курс: {self.course}')
        print(f'Средний балл: {sum(self.marks) / len(self.marks)}')


student = Student('Иван', 'Иванов', 2, [8, 6, 4])
student.get_info()
