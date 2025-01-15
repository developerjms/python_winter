import os           # 회원 추가, 검색, 삭제, 수정
import sys
import pymysql 
import member_sql as memsql
import dbconn
                   
# def mydbconn():
#     conn = pymysql.connect(host='localhost',user='root', password='1234', database='world',port=3306)
#     return conn

def screen():
    print('## 간단한 회원관리 ##')
    print('1.회원추가 2.회원목록 3.회원찾기 4.회원수정 5.화면클리어 6.회원삭제 7.탈퇴회원출력 8.탈퇴회원복귀 9.종료')

def memberADD():
    name = input('->이름: ')
    email = input('->이메일: ')
    age = input('->나이: ')
    
    # 디비연동코드 부분
    try : 
        conn = dbconn.mysql_world_conn()
        with conn.cursor() as curs:
            # sql_INSERT = """INSERT INTO MEMBER (name, email, age) VALUES (%s, %s, %s)"""
            curs.execute(memsql.insert_member_query(), (name, email, age))
    
        conn.commit()  # 디비에 삽입쿼리에 대한 결과를 완전 저장.
        print(f'{name},{email},{age}의 회원이 추가됨.')
    finally:
        conn.close()

def memberAlllist():
    print('------- 회원 정보 -------')
    # 디비연동코드 부분
    try:
        conn = dbconn.mysql_world_conn()
        with conn.cursor() as curs:
            # sql_SELECT = "SELECT * FROM member"
            curs.execute(memsql.select_member_query())
            rows = curs.fetchall()
            print('NO \t NAME \t\t EMAIL \t\t AGE \t DELYN')
            for row in rows:
                print(f'{row[0]} \t {row[1]} \t  {row[2]} \t {row[3]} \t {row[4]}')
    finally:
        conn.close()
        
def memberDELLIST():
    print('------- 탈퇴 회원 정보 -------')
    # 디비연동코드 부분
    try:
        conn = dbconn.mysql_world_conn()
        with conn.cursor() as curs:
            # sql_SELECT = "SELECT * FROM member"
            curs.execute(memsql.select_member_query_del())
            rows = curs.fetchall()
            print('NO \t NAME \t\t EMAIL \t\t\t AGE \t DELYN')
            for row in rows:
                print(f'{row[0]} \t {row[1]} \t  {row[2]} \t {row[3]} \t {row[4]}')
    finally:
        conn.close()
        
def memberDELList():
    print()
    
def memberSearch():  # 회원 1명
    name = input('검색할 이름: ')
    # 디비연동코드 부분
    try:
        conn = dbconn.mysql_world_conn()
        with conn.cursor() as curs:
            # sql_SELECT = "SELECT * FROM member WHERE name=%s"
        
            curs.execute(memsql.select_member_one_query(), name)
            rows = curs.fetchall()
            
            for row in rows:
                print(f'{row[0]} \t {row[1]} \t  {row[2]} \t {row[3]}')
    finally:
        conn.close()

def memberModify():  # 회원정보 수정( 이메일, 나이 )
    name = input('수정할 이름: ')
    
    try :
        conn = dbconn.mysql_world_conn()
        with conn.cursor() as curs:
            # sql_SELECT = "SELECT * FROM member WHERE name=%s"
            curs.execute(memsql.select_member_one_query(), name)
            rows = curs.fetchall()
    
        if not rows:
            print('없음')
        else:        
            for row in rows:
                print(f'{row[0]} \t {row[1]} \t  {row[2]} \t {row[3]}')
            
            mo_email = input('변경이메일: ')
            mo_age = input('변경나이: ')        
            with conn.cursor () as curs:
                # sql_UPDATE = """UPDATE member SET email=%s, age=%s WHERE name=%s"""
                curs.execute(memsql.update_member_query(), (mo_email, mo_age, name))
                conn.commit()  # 완전 변경확정
                print('변경되었음.')
    finally:
        conn.close()
        
def memberDEL():
    name = input('삭제할 사용자이름: ')
    try:
        conn = dbconn.mysql_world_conn()
        with conn.cursor () as curs:
            curs.execute(memsql.select_member_one_query(), name)
            rows = curs.fetchall()
        
        if not rows:
            print('없음')
        else:        
            for row in rows:
                print(f'{row[0]} \t {row[1]} \t  {row[2]} \t {row[3]}')
            mem_no = row[0] # 삭제할 회원 번호를 다른 변수에 저장.        
            with conn.cursor() as curs:
                curs.execute(memsql.delete_member_query_y(), (mem_no))
                conn.commit() # 완전 변경확정
            print('삭제되었음.')
    finally:
        conn.close()


def memberMembership():
    name = input('회원복귀할 이름름: ')
    try:
        conn = dbconn.mysql_world_conn()
        with conn.cursor () as curs:
            curs.execute(memsql.select_member_one_query(), name)
            rows = curs.fetchall()
        
        if not rows:
            print('없음')
        else:        
            for row in rows:
                print(f'{row[0]} \t {row[1]} \t  {row[2]} \t {row[3]}')
            mem_no = row[0] # 삭제할 회원 번호를 다른 변수에 저장.        
            with conn.cursor() as curs:
                curs.execute(memsql.delete_member_query_n(), (mem_no))
                conn.commit() # 완전 변경확정
            print('회원복귀되었음.')
    finally:
        conn.close()

        
# 2025년 1월 17일 오전 9:19
# 수정자 : 정명수
# 수정사항 : 
    
        
if __name__ == '__main__':
    while True:
        screen()
        choice =  input('-> ')
        if choice == '1':
            memberADD()         # 회원추가             
        elif choice == '2':
            memberAlllist()     # 회원전체출력
        elif choice == '3':
            memberSearch()      # 회원검색
        elif choice == '4':
            memberModify()      # 회원수정
        elif choice == '5':
            os.system('cls')    # 화면클리어( 맥은 'clear' )
        elif choice == '6':
            memberDEL()         # 회원삭제제
        elif choice == '7':
            memberDELLIST()     # 삭제한 회원리스트 출력
        elif choice == '8':
            memberMembership()  # 회원복귀귀    
        elif choice == '9':
            sys.exit(1)
        else:
            print('잘못된 번호, 다시 입력바람.')


# CREATE TABLE world.member (
#   mem_no INT NOT NULL AUTO_INCREMENT,
#   name VARCHAR(50) NULL,
#   email VARCHAR(100) NULL,
#   age VARCHAR(45) NULL,
#   PRIMARY KEY (mem_no));