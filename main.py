class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def result(self):
        avg = self.average()
        if avg >= 85:
            return "A'lo"
        elif avg >= 70:
            return "Yaxshi"
        elif avg >= 50:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"


student = Student("Jahongir")
student.add_grade(90)
student.add_grade(85)
student.add_grade(78)

print("O‘rtacha ball:", student.average())
print("Natija:", student.result())
