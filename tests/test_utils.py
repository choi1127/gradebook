# project_root_pkg > tests > test_utils.py

# tests/test_utils.py

import unittest
from gradebook.utils import mean, letter_grade


class TestUtils(unittest.TestCase):

    def test_mean(self):
        # 일반적인 평균 계산
        self.assertEqual(mean([10, 20, 30]), 20)
        # 빈 리스트일 경우 0.0 반환
        self.assertEqual(mean([])
, 0.0)

    def test_letter_grade(self):
        # A, B, C, D, F 학점 테스트
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "B")
        self.assertEqual(letter_grade(75), "C")
        self.assertEqual(letter_grade(65), "D")
        self.assertEqual(letter_grade(50), "F")


if __name__ == "__main__":
    unittest.main()