import JJ_menu as menu
import datetime as dt


def lib_term() :
    book = open("book_list.txt", 'r')
    menu.lib_list()

    count = 1;

    reader = book.readlines()
    
    for line in reader:
        
        line = line.strip()
        print(count,"번 | ",end="")
        print(line)
        
        
        count += 1

    book.close()

def add() :
    book = open("book_list.txt", 'a')
    
    menu.lib_add()
    year, month, day, name = input("입력: ").split()
    year = int(year); month = int(month); day = int(day)

    first = dt.date(year, month, day)
    last = first + dt.timedelta(days=14)
    
    data = "대출일 : %d.%d.%d | 반납일 : %d.%d.%d | 책 : %s\n" % (year, month, day, last.year, last.month, last.day, name)
    book.write(data)

    print("\n") 
    print("===================================")
    print("")
    print("대출하신 책의 내역입니다")
    print(data)
    print("===================================")

    book.close()

def remove() :

    menu.lib_remove()
    select = int(input("선택: "))

    with open("book_list.txt", 'r+') as remove:
        target = remove.readlines()
        remove.seek(0)
        cnt = 0

        for line in target:
            cnt += 1
            
            if cnt != select:
                remove.write(line)
                
        remove.truncate() 

    menu.lib_remove_c()

def c() :
  while True: #무한반복
    menu.lib_m() #메뉴 UI 출력
    select = int(input("선택 : ")) #선택값 입력

    if select == 1: #도서관 운영시간
        menu.lib_time()
        input("계속하려면 <Enter>를 입력하세요")
        

    elif select == 2: #대출기간 확인
        lib_term()
        
        

    elif select == 3: #도서 대출
        add()

        

    elif select == 4: #도서 반납
        remove()

        
        

    elif select == 0: #종료 break 실행 (0)
        
        break

    else :
        menu.num_error() #if문 이외 오류 출력 (?)
  
  return

