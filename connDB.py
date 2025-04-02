import pymysql
import datetime

def connectionDB():
    try:
        # MySQL 연결
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='jj103802##',
            db='PizzaOrder'
        )

    # 실행 시 주석 풀고 실행 (db 연결 확인) -> 평상시엔 나오면 안되니깐 주석처리
        print("연결 성공:", datetime.datetime.now())    # 현재 시간 출력
        return conn

    except pymysql.MySQLError as e:
        print("연결 실패:", e)
        return None