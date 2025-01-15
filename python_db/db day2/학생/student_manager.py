from dbconn1 import mysql_world_conn
from datetime import datetime
#import dbcoon
import query #쿼리 함수모음
import os

#데이터베이스 초기화
def init_db():
    try:
        conn = mysql_world_conn()
        cursor = conn.cursor()
        #학생 테이블 생성 students
        cursor.execute(query.create_student_table())
        #수강 테이블 생성 enrollments
        cursor.execute(query.create_enrollments_table())
        conn.commit() #확약
        print('두개의 테이블이 초기화되었습니다.(students,enrollments)')
    except Exception as e:
        print(f'DB 초기화 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
def add_student(name,age,grade):
    try:
        conn= mysql_world_conn()
        cursor = conn.cursor()
        cursor.execute(query.insert_student(), (name,age,grade))
        conn.commit()
        print(f'학생 {name}이 추가 되었습니다.')
    except Exception as e:
        print(f'학생 추가 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
def add_enrollment(student_id, course_name, enrollment_date):
    try:
        conn = mysql_world_conn()
        cursor = conn.cursor()
        cursor.execute(query.insert_enrollment(), (student_id, course_name, enrollment_date))
        conn.commit()
        print(f'학생  ID {student_id}의 수강 정보가 추가되었습니다.')
        
    except Exception as e:
        print(f'수강 정보 추가 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
# 학생 및 수강 정보 조회(조인)
def view_students_with_enrollments():
    try:
        conn = mysql_world_conn()
        cursor = conn.cursor()
        cursor.execute(query.select_student_with_enrollments())
        rows = cursor.fetchall() # select만 사용하는 함수
        if rows:
            for row in rows:
                print(f'학생 ID: {row[0]}, 이름 : {row[1]}, 나이: {row[2]}, 학년:{row[3]}, '
                    f'수강과목 : {row[4] if row[4] else "없음"}, 수강 날짜: {row[5] if row[5] else "없음"} ')
        else:
            print('조회할 학생 및 수강 정보가 없습니다.')    
    except Exception as e:
        print(f'조회 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

#특정 학생 조회
def view_students_whith_enrollments_one(student_name):
    try:
        conn = mysql_world_conn()
        cursor = conn.cursor()
        cursor.execute(query.select_student_with_enrollments_one(), (student_name))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f'학생 ID: {row[0]}, 이름 : {row[1]}, 나이: {row[2]}, 학년:{row[3]}, '
                    f'수강과목 : {row[4] if row[4] else "없음"}, 수강 날짜: {row[5] if row[5] else "없음"} ')
        else:
            print('조회되는 수강 정보가 없습니다.')
    except Exception as e:
        print(f'조회 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

#학생 정보 수정
def update_studnets(student_id, studnet_age, student_grade):
    try:
        conn = mysql_world_conn()
        cursor = conn.cursor()
        
        #학생 정보를 보여줌
        cursor.execute(query.select_students_one(), (student_id))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f'수정전 학생 ID: {row[0]}, 이름: {row[1]}, 나이: {row[2]}, 학년: {row[3]}, 등록일: {row[4]}')
                
        
        cursor.execute(query.update_student(), (studnet_age, student_grade, student_id))
        conn.commit()
        print('학생 정보 수정이 완료되었습니다.')
    except Exception as e:
        print(f'조회 중 오류 발생: {e}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
if __name__ == "__main__":
    init_db()
    while True:
        print("\n학생 및 수강 관리 시스템")
        print("1. 학생 추가")
        print("2. 학생 수강 정보 추가")
        print("3. 학생 및 수강 정보 조회")
        print("4. 학생 및 수강 정보 조회")
        print("5. 학생 정보 수정")
        print("6. 종료")
        print("7. 화면클리어")
        choice = input("선택: ")
        
        if choice == '1':
            try:
                name = input('이름: ')
                age = int(input('나이: '))
                grade = input('학년: ')
                add_student(name,age,grade)
            except ValueError:
                print("입력값이 유효하지 않습니다. 숫자와 텍스트를 정확히 입력하세요.")
                
        elif choice == '2':
            try:
                student_id = int(input('학생 ID: ')) #학생ID는 student 테이블의 id필드로 한다.
                course_name = input('수강 과목명: ')
                enrollment_date = input('수강 날짜(YYYY-MM-DD): ')
                # 날짜 형식 검증
                datetime.strptime(enrollment_date, '%Y-%m-%d')
                add_enrollment(student_id, course_name, enrollment_date)    
            except ValueError:
                print('입력값이 유효하지 않습니다. 숫자와 텍스트를 정확히 입력하세요.')
        
        elif choice =='3':
            view_students_with_enrollments()
            
        elif choice =='4':
            try:
                student_name = input('학생 이름 : ')
                view_students_whith_enrollments_one(student_name)
            except ValueError:
                print('입력값이 유효하지 않습니다. 숫자와 텍스트를 정확히 입력하세요.')
            
        elif choice =='5':
            try:
                student_id = int(input('학생 ID : '))
                studnet_age = int(input('나이(수정) : '))
                student_grade = input('학년(수정) : ')
                update_studnets(student_id, studnet_age, student_grade)
            except ValueError:
                print('입력값이 유효하지 않습니다. 숫자와 텍스트를 정확히 입력하세요.')
                
        elif choice =='6':
            print('프로그램 종료.')
            break
        
        elif choice=='7':
            os.system('cls')
            
        else:
            print('잘못된 입력입니다. 다시 시도하세요.')

