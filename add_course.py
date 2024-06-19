import os
import django
import pandas as pd

# Django 설정을 초기화합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Course 모델을 임포트합니다.
from timetable.models import Course

def add_course():
    # CSV 파일을 읽습니다.
    df = pd.read_csv('2024-1-preprocessed.csv')
    
    # 데이터프레임의 각 행을 반복 처리합니다.
    for index, row in df.iterrows():
        # Course 인스턴스를 생성하고 저장합니다.
        new_course = Course(
            major=row['학과(부)'],
            year=row['학년'],
            classification=row['이수구분'],
            course_code=row['학수번호'],
            course_name=row['교과목명'],
            professor=row['담당교수'],
            timetable_period=row['시간표(교시)'],
            timetable_time=row['시간표(시간)'],
            credits=row['학점'],
            class_type=row['수업유형'],
        )
        new_course.save()
        print(f"Added: {new_course}")

# 스크립트를 실행하는 메인 부분
if __name__ == "__main__":
    add_course()