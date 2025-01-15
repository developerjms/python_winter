import book_query_sql as wq
import book_dbconn as bdb

connection = bdb.mysql_book_conn()

# SELECT

def view_book_all():
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.book_select_sql())
            results = cursor.fetchall()
            for row in results:
                print(row)
            print('모든책 정보출력완료.')
    except Exception as e:
        print(f'모든책 찾기 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
        
def view_book(book_no):
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.book_select_sql_1(), book_no)
            results = cursor.fetchall()
            for row in results:
                print(row)
            print('책 정보출력완료.')
    except Exception as e:
        print(f'책 정보 찾기 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()

def view_member_all():
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.member_select_sql())
            results = cursor.fetchall()
            for row in results:
                print(row)
            print('모든회원정보출력완료.')
    except Exception as e:
        print(f'모든회원 찾기 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()

def view_member(member):
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.member_select_sql_1(), member)
            results = cursor.fetchall()
            for row in results:
                print(row)
            print('한명 회원정보출력완료.')
    except Exception as e:
        print(f'모든회원 찾기 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
        
def view_order_all():
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.order_select_sql())
            results = cursor.fetchall()
            for row in results:
                print(row)
            print('모든정보출력완료.')
    except Exception as e:
        print(f'모든회원 찾기 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
            
def view_book_order(order_no):
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.member_select_sql_1(), order_no)
            results = cursor.fetchall()
            for row in results:
                print(row)
            print('한명 회원정보출력완료.')
    except Exception as e:
        print(f'모든회원 찾기 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
            
# INSERT

def insert_book(book_insert_data):
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.book_insert_sql(), book_insert_data)
            connection.commit()
            print('책 추가 완료')
    except Exception as e:
        connection.rollback()
        print(f'책 추가 중 오류발생: {e}')
    finally:
        if cursor:
            cursor.close()

def insert_member(member_insert_data):
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.member_insert_sql(), member_insert_data)
            connection.commit()
            print('회원 추가 완료')
    except Exception as e:
        connection.rollback()
        print(f'회원 추가 중 오류발생: {e}')
    finally:
        if cursor:
            cursor.close()
        
# UPDATE        

def update_member(mem_no, mem_addr, email_id, htel_no):
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.member_update_sql(), (mem_addr, email_id, htel_no, mem_no))
            connection.commit()
            print('회원 업데이트 완료')
    except Exception as e:
        connection.rollback()
        print(f'회원 업데이트 중 오류발생: {e}')
    finally:
        if cursor:
            cursor.close()
        
def update_book(book_no, book_type, price):
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.book_update_sql(), (book_type, price, book_no))
            connection.commit()
            print('책 정보 업데이트 완료')
    except Exception as e:
        connection.rollback()
        print(f'책 업데이트 중 오류발생: {e}')
    finally:
        if cursor:
            cursor.close()
        