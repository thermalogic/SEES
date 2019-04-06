from grade import *

ug1 = UG('Jane Doe', 2014)
# 1 creat the course named sixHundred
sixHundred = Grades()

# 2 some students taking a course named sixHundred
sixHundred.addStudent(ug1)

# 3 add Grades of students
sixHundred.addGrade(ug1, 85)
sixHundred.addGrade(ug1, 90)
print('The student grades:', sixHundred.grades)
# 4  produce a grade report
print(gradeReport(sixHundred))