"""Make a class structure in python representing people at school. Make a base class called Person, a class called
Student, and another one called Teacher. Try to find as many methods and attributes as you can which belong to
different classes, and keep in mind which are common and which are not. For example, the name should be a Person
attribute, while salary should only be available to the teacher. """
import datetime


class Person:

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.year = datetime.datetime.today().year
        self.age = age

    def greeting(self):
        print(f'Hello, I am {self.name} {self.last_name}.')


class Teacher(Person):

    def __init__(self, name, last_name, age, payment):
        super().__init__(name, last_name, age)
        self.salary = payment

    def increase_payment(self, percent):
        self.salary += round(self.salary * percent / 100)

    def decrease_payment(self, percent):
        self.salary -= round(self.salary * percent / 100)


class Student(Teacher):

    def __init__(self, name, last_name, age, payment):
        super().__init__(name, last_name, age, payment=0)
        self.scholarship = payment

    def increase_payment(self, percent):
        self.scholarship += round(self.scholarship * percent / 100)

    def decrease_payment(self, percent):
        self.scholarship -= round(self.scholarship * percent / 100)


if __name__ == '__main__':
    my_person = Person('Liudmyla', 'Yasinkovska', 25)
    print(my_person.age)
    my_person.greeting()
    new_teacher = Teacher('Bob', 'Jones', 45, 3000)
    print(new_teacher.salary)
    new_teacher.increase_payment(10)
    print(new_teacher.salary)
    new_student = Student('Liudmyla', 'Yasinkovska', 25, 100)
    print(new_student.scholarship)
    print(new_student.salary)
    new_student.increase_payment(5)
    print(new_student.scholarship)
    print(new_student.salary)
