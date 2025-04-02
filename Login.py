import connDB
class Personal_Info:
        
    def __init__(self, id, passwd, address):
        self.id = id            # 아이디
        self.passwd = passwd    # 패스워드
        self.address = address  # 주소
    
    def login(self):    # 로그인 함수
            # 입력받기
        self.id = input('아이디: ')
        self.passwd = input('비밀번호: ')
        self.address = input('주소: ')

        conn = connDB.connectionDB()

        cursor = conn.cursor()
            ## 중복 삽입 x 설정
        if():
            pass
        else:   # 신규가입
            sql = 'INSERT INTO users (name, address, passwd) values ( %s, %s, %s)'      # d = 정수, s = 문자
            val = (self.id, self.address, self.passwd)

            cursor.execute(sql, val)
            conn.commit()    # 저장
        cursor.close()    
