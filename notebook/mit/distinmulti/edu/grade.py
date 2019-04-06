from .student import *

class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list [student1,studen2,...]
        # dict {student1.IdNum:[grade1,grade2,...],student2.IdNum:[grade1,grade2,...],...}
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:  # return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True

        # return copy of list of students
        # return self.students[:]

        # the better solution: generator
        for s in self.students:
            yield s


def gradeReport(course):
    """Assumes course is of type Grades"""

    report = ''
    # the data be accessed only through the object's methods. information hiding.
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        # the data be accessed only through the object's methods. information hiding.
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = (report + '\n'
                      + str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report = (report + '\n'
                      + str(s) + ' has no grades')
    return report
