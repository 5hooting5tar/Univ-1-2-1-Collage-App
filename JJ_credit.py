import JJ_menu as menu

name = ['김해울', '정찬호', '나성빈', '진예섭']
num = [202268023, 202268025, 202268031, 202268029]
role =['main', 'lib', 'memo', 'dday']



def credit_name() : #학번-이름 출력
  print('학번-이름 ')
  for i in range(len(name)):
    print(num[i],':' , name[i])

def credit_part() : #이름-역할 출력
  print('이름-역할 ')
  for i in range(len(name)):
      print(name[i], ':' , role[i])

def selection() :
  while True: #무한반복
    menu.credit() #메뉴 UI 출력
    select = int(input("선택 : ")) #선택값 입력

    if select == 1: #학번-이름 (1)
        credit_name()

        input("계속하려면 <Enter> 를 입력하세요. ")

    elif select == 2: #이름-역할 (2)
        credit_part()
        
        input("계속하려면 <Enter> 를 입력하세요. ")
        

    elif select == 0: #종료 break 실행 (0)
        break

    else :
        menu.num_error() #if문 이외 오류 출력 (?)
  
  return






