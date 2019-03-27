from datetime import date, timedelta, datetime
from hashlib import sha256

class Person:
    def __init__(self, first_name, last_name, year):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def age(self):
        """
        use datetime module
        """

        difference = datetime.now() - datetime(year=self.year, month=1, day=1)
        return difference.days

    def __str__(self):
        return f'{self.first_name} is {self.age()} days old'

    def __repr__(self):
        return str(self)


jussi = Person("Jussi", "Ojala", 1981)
print(jussi)


# def get_average_age(people):
#     return sum(person.age for person in people) / len(people)

# people = [Person("John", "Smith", 1985), Person("mary", "smith", 1970)]

# print(get_average_age(people))

class Student:

    # the person parameter must be a Person object
    def __init__(self, person, password):
        """
        bonus(use sha256 hashing)
        """
        self.person = person
        self.password = password
        self.projects = []

    # use the full_name method for Person
    def get_name(self):
        return self.person.full_name()

    def check_password(self, password):
        return password == self.password

    def get_projects(self):
        return self.projects

    def add_project(self, project):
        self.projects.append(project)

person = Person('Jack', 'Jones', 1990)
student = Student(person, 'jackpassword123')

student.check_password('jackpassword123')

# challenge: modify Student class to include ID instead of name-password match
# and implement a function to assign project to a student by id
def assign(students, name, password, project):
    pass
