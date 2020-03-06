import datetime
from dateutil.relativedelta import relativedelta


class Person:

    def __init__(self, name):
        """Create a person：common attributes name and birthdate"""
        self.name = name  # 1 fullname:firstname lastname or 2 lastname
        try:
            lastBlank = name.rindex(' ')  # ' 'lastName
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name

        self.birthday = None

    def getName(self):
        """Returns self's full name"""
        return self.name

    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """Returns self's current age in years"""
        if self.birthday == None:
            raise ValueError
        relatyears = relativedelta(datetime.date.today(), self.birthday)
        return relatyears.years+round(relatyears.months/12, 1)

    def __lt__(self, other):
        """Returns True if self's name is lexicographically  less than other's name, 
           and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """Returns self's name"""
        return self.name


class MITPerson(Person):

    nextIdNum = 0  # identification number　- class

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1  # identification number

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(Student):
    pass
