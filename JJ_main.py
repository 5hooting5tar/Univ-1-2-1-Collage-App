#Project JJ Ver. 1.0
#Main Code

import JJ_lib as lib #도서관 기능 코드
import JJ_dday as dday #D-DAY 기능 코드
import JJ_memo as memo #메모 기능 코드
import JJ_menu as menu #메뉴 UI 코드
import JJ_credit as credit # 크레딧 UI 코드


menu.startup() #프로그램 실행 첫화면 출력

while True: #무한반복
    menu.main_m() #메뉴 UI 출력
    select = int(input("선택 : ")) #선택값 입력

    if select == 1: #도서관 기능 실행 (1)
        lib.c()

    elif select == 2: #DDAY 기능 실행 (2)
        dday.select()

    elif select == 3: #메모 기능 실행 (3)
        memo.test()

    elif select == 4: #Credit 실행 (4)
        credit.selection()

    elif select == 0: #종료 break 실행 (0)
        menu.shutdown()
        break

    else :
        menu.num_error() #if문 이외 오류 출력 (?)
    
