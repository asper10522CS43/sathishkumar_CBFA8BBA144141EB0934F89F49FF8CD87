
class student:

def __init__(self, name, roll_number, cgpa):

self.name = name

self.roll_number = roll_number

self.cgpa = cgpa

def sort students(student_list): sorted students = sorted(student_list,

key-lambda student:student.cgpa, reverse=True)

return sorted_students

students=[

student("jack","a124',10), student("hendry',125,9.6),

student(joel,a126,6.3),

student(lional, a127,8.6),

sorted_students = sort students(students)

for student in sorted_students:

print("Name: 0), Roll Number: (), CGPA:0}".format(student.name,

student.roll_number, student.cgpa))