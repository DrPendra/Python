class Student:
    '''
    #Avant avec Error
    def __init__(self, grades=[]):
        self.grades = grades
        self.count_grades = len(grades)
        if len(grades) == 0:
            self.academic_average = 0
        else:
            elf.academic_average = sum(grades) / len(grades)
    '''
    def __init__(self, grades=[10]):
        # the student will now have a default grade of 10 when he is created
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