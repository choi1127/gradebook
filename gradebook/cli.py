# project_root/gradebook/cli.py

import csv
"""
**실행형 명령줄 인터페이스(CLI)**
"""

from .models import Student, Gradebook


def load_students_from_csv(filepath):
    """CSV 파일에서 Student 객체를 로드"""
    students = []
    with open(filepath, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 스킵
        for row in reader:
            name = row[0]
            scores = [int(score) for score in row[1:]]
            students.append(Student(name, scores))
    return students


def run_cli():
    """CLI에서 실행할 때 호출"""
    print("Gradebook 실행 중...")
    try:
        # CSV 파일로부터 데이터 로드 (가정: students.csv 파일이 있다고 가정)
        students = load_students_from_csv("students.csv")
        gb = Gradebook()
        for student in students:
            gb.add_student(student)

        # 예제 사용: Student 객체 직접 추가
        gb.add_student(Student("Alice", [90, 85, 92]))
        gb.add_student(Student("Bob", [78, 75, 80]))
        gb.add_student(Student("Charlie", [65, 70, 60]))

    except FileNotFoundError:
        print("students.csv 파일이 없습니다. 기본 데이터 사용.")
        # students.csv 파일이 없을 때 기본 데이터 사용
        gb = Gradebook()
        gb.add_student(Student("Alice", [90, 85, 92]))
        gb.add_student(Student("Bob", [78, 75, 80]))
        gb.add_student(Student("Charlie", [65, 70, 60]))

    # 결과 출력
    print(f"\n[전체 학생 평균 점수: {gb.get_average():.2f}]")
    print("\n--- 학생별 결과 ---")
    for s in gb.get_students():
        print(f"이름: {s.name:<10} | 평균: {s.average():.1f} | 학점: {s.grade()}")