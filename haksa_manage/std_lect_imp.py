from std_lect import STUDENT
from file_util import *
import os


def std_lect_imp():
    print("학번을 입력하세요.")
    STUDENT.std_id = input()
    print("이름을 입력하세요.")
    STUDENT.name = input()
    print("나이를 입력하세요.")
    STUDENT.age = input()
    os.system('clear')
    std_lect_show()


def std_lect_show():
    print("==========================")
    print(STUDENT.std_id + " 수강신청서")
    print("==========================")
    print("이름: " + STUDENT.name)
    print("나이: " + STUDENT.age)
