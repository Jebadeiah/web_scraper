class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = name[0] + last_name + str(birth_year)


st_name = input()
st_last = input()
st_year = input()
student = Student(st_name, st_last, st_year)
print(student.student_id)
