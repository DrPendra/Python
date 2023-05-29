from context import src

import pytest

@pytest.fixture
def student():
    return src.StudentV2()


def test_create_student_grades(student):
    grade = student.grades
    assert grade == []
def test_create_student_average(student):
    assert student.academic_average == 0

def test_add_grades(student):
    student.add_grade(12)
    assert student.academic_average == 12
