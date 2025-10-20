# project_root/gradebook/models.py

"""
Student | Gradebook 정의 파일
"""

from .utils import mean, letter_grade


class Student:
    """학생 클래스"""
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def set_scores(self, scores):
        self.scores = scores

    def average(self):
        """성적 평균"""
        if not self.scores:
            return 0.0
        return mean(self.scores)

    def grade(self):
        """학점 계산"""
        return letter_grade(self.average())

    def __repr__(self):
        return f"Student(name={self.name!r}, scores={self.scores})"


class Gradebook:
    """학점 관리부 클래스"""
    def __init__(self):
        self._students = {}  # {이름: Student 객체}

    def add_student(self, student):
        """학생 추가"""
        self._students[student.name] = student

    def get_average(self):
        """전체 학생 성적 평균"""
        return sum(
            s.average() for s in self._students.values()
        ) / len(self._students) if self._students else 0.0

    def get_students(self):
        """학생 목록 반환"""
        return self._students.values()

    def __repr__(self):
        return f"Gradebook({list(self._students.keys())})"