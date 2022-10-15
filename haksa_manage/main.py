from _menu import *
from std_lect_imp import *


def main():
    while(1):
        if(main_menu() == 1):
            print("학생 정보 입력")
            std_lect_imp()
            break
        elif main_menu() == 2:
            print("학생 정보 보기")
            break
        elif main_menu() == 3:
            print("학생 정보 삭제")
            break
        elif main_menu() == 4:
            print("학생 정보 수정")
            break
        elif main_menu() == 5:
            print("정보 검색")
            break
        elif main_menu() == 6:
            print("데이터 초기화")
            break
        elif main_menu() == 7:
            print("데이터 자동 생성")
            break
        elif main_menu() == 8:
            print("종료")
            break
        else:
            print("1~8의 숫자를 입력하세요.")


main()
