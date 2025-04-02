import Button
class Pizza:
    def __init__(self):
            # 메뉴판
        self.menus = ['페퍼로니피자','스테이크피자','시푸드피자']
            # 가격판
        self.price = [29000,32000,32000]
        
        # 메뉴 보여주기, count
    def show_menu(self):
        print('\n 피자를 선택하세요.')
        for idx, item in enumerate(self.menus):
            print(f"{idx +1}. {item} ({self.price[idx]}원)")
        choice = input("번호를 입력하고 Enter를 누르세요 (다음단계:n, 이전단계:p, 주문완료:f)")
        count  = 0
        return choice, count, self.menus, self.price
            
        # 피자 선택
    def choose_pizza(self):           
            # pizza 변수에 선택한 피자 넣기
            # 버튼 선택
        Button.button.pizza_button(self.show_menu())
        
        # 가격 누적