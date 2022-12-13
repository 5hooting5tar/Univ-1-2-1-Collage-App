import datetime as dt #datetime 모듈 입력 - 날짜처리
import JJ_menu as menu #메뉴 UI 코드



def log_count() : #로그 20개 초과 카운트
    with open("dday_log.txt", 'r') as check: 
        l_count = int(1)
    
        while True:
            if check.readline()=='':
                break
            l_count += 1

    if l_count >= 20 : #로그 20개 초과 시 
        with open("dday_log.txt", 'r+') as remove:
            lines = remove.readlines() #전체 줄 읽기
            remove.seek(0) #0번째 줄로 이동
            remove.truncate() #현위치까지 남기기, 나머지 정리
            remove.writelines(lines[1:]) #1번 줄 땡기기



def calc_today() : #오늘 기준 디데이 계산
    log = open("dday_log.txt", 'a') #로그파일 오픈

    menu.dday_today() #UI 출력

    today = dt.date.today() #오늘 날짜 설정
    year1 = today.year; month1 = today.month; day1 = today.day #오늘 년,월,일 import
    
    year2, month2, day2 = input("입력: ").split() #끝 년,월,일 input
    year2 = int(year2); month2 = int(month2); day2 = int(day2) #input값 integer 변환
    target = dt.date(year2, month2, day2) #끝 날짜 설정

    calc = target - today #d-day 계산값 calc에 저장
    result = calc.days #calc의 days값 result에 저장

    if result < 0 : #날짜 오류 테스트 - D-day가 음수 일 때 (날짜 오류)
        menu.input_error()
        log.close()
        return
    elif result == 0 : #D-day일 때 result에 'Day' 저장
        result = str(result)
        result = 'Day'

    data = "%d년 %d월 %d일 ~ %d년 %d월 %d일 | D-%s\n" % (year1, month1, day1, year2, month2, day2, result)
    log.write(data) #data 출력 log에 기록

    print("\n") #계산결과 UI 출력
    print("===================================")
    print("")
    print("D-Day 계산 결과")
    print(data)
    print("===================================")
    
    log.close() #로그파일 종료



def calc_select() : #선택 기준 디데이 계산
    log = open("dday_log.txt", 'a') #로그파일 오픈

    menu.dday_sel() #UI 출력

    year1, month1, day1 = input("시작 일자 입력: ").split() #시작 년,월,일 input
    year1 = int(year1); month1 = int(month1); day1 = int(day1) #input값 integer 변환
    start = dt.date(year1, month1, day1) #시작 날짜 설정
    
    year2, month2, day2 = input("끝 일자 입력: ").split() #끝 년,월,일 input
    year2 = int(year2); month2 = int(month2); day2 = int(day2) #input값 integer 변환
    end = dt.date(year2, month2, day2) #끝 날짜 설정

    calc = end - start #d-day 계산값 calc에 저장
    result = calc.days #calc의 days값 result에 저장

    if result < 0 : #날짜 오류 테스트 - D-day가 음수 일 때 (날짜 오류)
        menu.input_error()
        log.close()
        return
    elif result == 0 : #D-day일 때 result에 'Day' 저장
        result = str(result)
        result = 'Day'

    data = "%d년 %d월 %d일 ~ %d년 %d월 %d일 | D-%s\n" % (year1, month1, day1, year2, month2, day2, result)
    log.write(data) #data 출력 log에 기록

    print("\n") #계산결과 UI 출력
    print("===================================")
    print("")
    print("D-Day 계산 결과")
    print(data)
    print("===================================")

    log.close() #로그파일 종료



def calc_list() : #디데이 계산 기록
    log = open("dday_log.txt", 'r') #로그파일 오픈
    menu.dday_list()

    lines = log.readlines()
    for line in lines:
        line = line.strip()
        print(line)

    log.close() #로그파일 종료
    

def select() : #디데이 메뉴  
    while True: #무한반복
        menu.dday_m() #메뉴 UI 출력
        log_count() #로그 20개 초과 체크
        select = int(input("선택 : ")) #선택값 입력

        if select == 1: #디데이 계산 - 오늘 기준 (1)
            calc_today()

        elif select == 2: #디데이 계산 - 선택날짜 기준 (2)
            calc_select()

        elif select == 3: #계산 기록 (3)
            calc_list()

        elif select == 0: #종료 break 실행 (0)
            break

        else :
            menu.num_error() #if문 이외 오류 출력 (?)

    return #메인으로 돌아가기

