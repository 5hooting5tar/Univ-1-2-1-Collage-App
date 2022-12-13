import JJ_menu as menu #메뉴 UI 코드
import datetime as dt



def memo_list() : #메모 보기
    memo = open("memo_list.txt", 'r')
    menu.memo_list()
    
    lines = memo.readlines()
    for line in lines:
        line = line.strip()
        print(line)

    memo.close()



def memo_withdday() : # D-day 기록
    menu.memo_withdday()

    select1 = str(input("선택 : "))
    if select1 == "y" or select1 == "Y":
        print("1번을 누르면 과제의 남은 기간을  볼 수 있습니다")
        print("2번을 누르면 메모를 추가합니다.")
        select2 = int(input("선택 : ")) #선택값 입력

        if select2 == 1: 
            memo_add_dday()
  
        elif select2 == 2:
            memo_add()
    elif select1 == "n" or select1 == "N":
        print("디데이 일정을 기록하지 않습니다.")
        memo_add()   
    else :
        menu.num_error()




def memo_add_dday() : #메모
    memo  = open("memo_list.txt",'a') # 추가모드로 파일 열기
    print("**경고**날짜 입력후 메모 작성시 작성 메모는 띄어쓰기를 지원하지 않습니다.")
    
    menu.memo_add_dday()
    
    print("시작일을 입력해주세요") # 시작일
    year1, month1, day1, todo = input("입력: ").split() #각 변수에 입력하여 저장
    year1 = int(year1); month1 = int(month1); day1 = int(day1) #각 변수에 자료형을 int로 하여 저장
    first_date = dt.date(year1, month1, day1) # date()함수를 통해 입력된 변수로 날짜를 계산, first_date에 저장
    
    print("제출일을 입력해주세요") # 제출일
    year2, month2, day2 = input("입력: ").split()
    year2 = int(year2); month2 = int(month2); day2 = int(day2)
    target_date = dt.date(year2, month2, day2)

    calc = target_date - first_date #제출일 - 시작일 을 calc에 저장
    result = calc.days
    
    data = "시작일 : %d.%d.%d | 제출일 : %d.%d.%d | 남은 기간입니다: D-%s | 과제 : %s\n" % (year1, month1, day1, year2, month2, day2, result, todo)
    memo.write(data)
    
    
    print("\n") 
    print("===================================")
    print("")
    print("과제의 남은 기간입니다")
    print(data)
    print("===================================")






def memo_add() :# 메모 추가하기   #  #메모장에 메모가 저장되게 하기 
    menu.memo_add()
    print("공백을 입력하면 메모를 종료합니다.")
    print("***********************************") 
    memo = open("memo_list.txt", 'a')# 추가모드로 파일 열기
    while True: # 반복 루프
        
        str = input('입력란: ')# 문자 입력 str에 저장하기 
        
        if not str:# str이 없음 공백(str에 저장 된 것이 없음) 
            break# 반복문 탈출
        
        memo.write(str + '\n')# 문자열을 '\n'을 추가하여 메모장에 쓰기
    memo.close() # 메모 닫기 
        
    menu.memo_add_c() # 메뉴 memo_add_c 호출
    
        
       
        

    

def memo_write() :# 메모 쓰기 #메모장에 메모 저장하기 #기존메모는 사라짐
    menu.memo_write()
    print("공백을 입력하면 메모를 종료합니다.")
    print("***********************************")
    memo = open("memo_list.txt", 'w') # 쓰기모드로 파일 열기
    while True: # 반목 루프
        str = input("입력란: ")# 문자 입력 str에 저장하기
        
        if not str:# str이 없음, 공백(str에 저장 된 것이 없음)
            break# 반복문 탈출

        memo.write(str + '\n')# 문자열을 '\n'을 추가하여 메모장에 쓰기
    memo.close() # 메모 닫기
    print("메모 쓰기를 종료합니다!") #"메모 쓰기를 종료합니다! 출력
    
 



def memo_remove() :

    menu.memo_remove()
    select = int(input("선택: "))

    with open("memo_list.txt", 'r+') as remove:
        target = remove.readlines()
        remove.seek(0)
        cnt = 0

        for line in target:
            cnt += 1
            
            if cnt != select:
                remove.write(line)
                
        remove.truncate() 

    menu.memo_remove_c()




subject = ["논리적사고와글쓰기"," 이산수학", "소프트웨어기초설계", "C프로그래밍", "생활영어회화", "선형대수"]
    
def test() :
    while True: #무한반복
        menu.memo_m() 

        select = int(input("선택 : ")) #선택값 입력

        if  select == 1: # 과목 보기(1)
            print(subject)
        
        elif select == 2: #메모 보기 (2)
            memo_list()

        elif select == 3: #메모 쓰기 (3)
            memo_write()

        elif select == 4: #메모 추가, 과제 dday 7일 (4)
            memo_withdday()
         
        elif select == 5: #메모 삭제 (5)
            memo_remove()               
 
        elif select == 0: #종료 break 실행 (0)
            break

        else :
            menu.num_error() #if문 이외 오류 출력 (?)

    return #메인으로 돌아가기

