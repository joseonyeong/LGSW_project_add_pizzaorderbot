import Login
import connDB   # db 연결 확인
import Pizza

if __name__ == '__main__':
    print('피자 주문을 시작합니다.', end='\n')
    
    user = Login.Personal_Info("","","")    # 초기화
    user.login()    # 로그인 실행
    print(f"{user.id}님 환영합니다.")
    
    ## 피자 메뉴 보여주기 + 피자 선택
    Pizza.Pizza()
    
    
