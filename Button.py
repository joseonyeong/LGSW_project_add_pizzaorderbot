## 다음 단계 : n
## 이전 단계 : p
## 주문 완료 : f
import connDB

class button():
        # 피자 버튼
    def pizza_button(choice, count, menus, price):
            
            # db 연결
        conn = connDB.connectionDB()     
            # 커서, close 필요
        cusor = conn.cursor()
        
        while True:
            if choice.upper() == 'F':
                ## 주문 내역
                pass
                break   # 종료
            elif choice.upper() == 'N':
                    # 피자 건너뛰고 다음 단계인 토핑을 누를 경우우
                if count == 0:
                    print('피자를 먼저 선택해주세요.')
                        # while문??
                    pass
                if choice.isdigit():    # 숫자만만
                    index = int(choice)
                    if int(choice) < len(menus) + 1:
                            # sql에 인서트해야됨
                        sql = 'INSERT INTO users (pizza, price) VALUES (%s, %s)'
                        val = (menus[int(choice)], price[int(choice)])  # 선택한 피자
                        print(f"선택된 메뉴: {menus[int(choice)]}, 가격: {price[int(choice)]}")

                    else:
                        print('다시 입력하세요.')
        return True
        
        # 토핑 버튼
        
        # 사이드 버튼
        
        # 드링크 버튼