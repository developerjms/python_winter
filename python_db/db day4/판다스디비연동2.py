import pandas as pd
import pymysql

# CSV 파일 경로를 지정하세요
file_path = r"C:\Users\USER\Desktop\python\python\db day4\bicycle.csv"


# CSV 파일을 데이터프레임으로 읽어오기
df = pd.read_csv(file_path, encoding='utf-8')

# 컬럼명을 Col1, Col2, ...로 변경 (선택사항)
df.columns = [f"Col{i+1}" for i in range(len(df.columns))]
print("변경된 컬럼명:", df.columns)

df_clean = df.dropna()

#MYSQL 연결 정보 설정
mysql_host = "localhost"
mysql_user = "root"
mysql_password = "1234"
mysql_database = "world"

#MYSQL 연결
try :
    connection = pymysql.connect(host='localhost', user='root', password='1234', database='world', port=3306, charset='utf8mb4')
    
    
    cursor = connection.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS bicycle (
        id INT AUTO_INCREMENT PRIMARY KEY,
        col1 VARCHAR(100),
        col2 VARCHAR(100),
        col3 VARCHAR(100),
        col4 VARCHAR(100),
        col5 VARCHAR(100),
        col6 VARCHAR(100),
        col7 VARCHAR(100),
        col8 VARCHAR(100),
        col9 VARCHAR(100),
        col10 VARCHAR(100),
        col11 VARCHAR(100)
    );
    """
    cursor.execute(create_table_query)
    print("테이블이 성공적으로 생성되었습니다.")
    
    for _, row in df_clean.iterrows():
        insert_query = """
        INSERT INTO bicycle (col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            col1 = VALUES(col1),
            col2 = VALUES(col2),
            col3 = VALUES(col3),
            col4 = VALUES(col4),
            col5 = VALUES(col5),
            col6 = VALUES(col6),
            col7 = VALUES(col7),
            col8 = VALUES(col8),
            col9 = VALUES(col9),
            col10 = VALUES(col10),
            col11 = VALUES(col11);
        """
        cursor.execute(insert_query, (
            row["Col1"], row["Col2"], row["Col3"], row["Col4"], row["Col5"],
            row["Col6"], row["Col7"], row["Col8"], row["Col9"], row["Col10"], row["Col11"]
    ))
    connection.commit()
    print("정보가 성공적으로 저장되었습니다.")
    
except Exception as e:
    print(f'오류 발생: {e}')
finally:
    if connection:
        connection.close()
        print('디비 연결 종료')