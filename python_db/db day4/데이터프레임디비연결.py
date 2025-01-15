import pandas as pd
import pymysql

# 학생 정보 데이터프레임 생성
data = {
    "StudentID": [1, 2, 3, 4, 5],       #학번
    "Name" : ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],  #이름
    'Age' : [20, 21, 22, 19, 23],       #나이
    'Score' : [85.5, 90.0, 78.0, 88.5, 92.0]    #점수
}
students_df = pd.DataFrame(data)

try :
    conn = pymysql.connect(host='localhost', user='root', password='1234', database='world', port=3306)
    cursor = conn.cursor()
    
    #테이블 생성
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students2 (
        studentsID INT PRIMARY KEY,
        name varchar(50),
        age int,
        score float
    )
    """
    cursor.execute(create_table_query)
    print('students2 테이블 생성 성공!')
    
    for _, row in students_df.iterrows():
        insert_query="""
        INSERT INTO students2 (Name, Age, Score)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Name=VALUES(Name),
            Age=VALUES(Age),
            Score=VALUES(Score)
        """
        cursor.execute(insert_query, (row['Name'], row['Age'], row['Score']))
    conn.commit()
    print('데이터 정보가 성공적으로 저장됨')
    
    
except Exception as e:
    print(f'오류 발생: {e}')
finally:
    if conn:
        conn.close()
        print('디비 연결 종료')