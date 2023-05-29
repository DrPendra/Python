class StudentV2:  # creation of a student class
    def __init__(self, grades=[]):
        # reset default grades to an empty list
        self.count_grades = len(grades)
        self.grades = grades
        if len(grades) == 0:
            self.academic_average = 0
        else:
            self.academic_average = sum(grades) / len(grades)


    def add_grade(self, grade):
        if (grade < 0) | (grade > 20):
            raise InvalidGrade("Grade should be between 0 and 20")
        else:
            self.grades = []
            self.grades.append(grade)
            if len(self.grades) == 0:
                self.academic_average = 0
            else:
                self.academic_average = sum(self.grades) / len(self.grades)

class InvalidGrade(Exception):
    pass