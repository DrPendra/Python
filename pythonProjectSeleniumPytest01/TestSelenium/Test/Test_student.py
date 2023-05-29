from context import src
# 3 test cases are defined in this test suite
def test_create_student_grades():
    student = src.Student()
    assert student.grades == [10]

def test_create_student_average():
    student = src.Student()
    assert student.academic_average == 10

def test_add_grades():
    student = src.Student()
    student.add_grade(12)
    assert student.academic_average == 12
