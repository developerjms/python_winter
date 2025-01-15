import world_query_sql as wq
import world_dbconn as wdb

connection = wdb.mysql_world_conn()

def insert_city_country(country_data, city_data):
    try:
        with connection.cursor() as cursor:
            #Execut queries in sseq
            cursor.execute(wq.insert_city_query().split(";\n\n")[0], country_data)
            cursor.execute(wq.insert_city_query().split(";\n\n")[1], city_data)
            connection.commit()
            print('Data sucessfully inserted into Country, City tables.')
    except Exception as e:
        connection.rollback()
        print(f'Error inserting data: {e}')
        
def insert_all(country_data, city_data, country_language_data):
    try:
        with connection.cursor() as cursor:
            #Execut queries in sseq
            cursor.execute(wq.insesrt_all_query().split(";\n\n")[0], country_data)
            cursor.execute(wq.insesrt_all_query().split(";\n\n")[1], city_data)
            cursor.execute(wq.insesrt_all_query().split(";\n\n")[2], country_language_data)
            connection.commit()
            print('Data sucessfully inserted into Country, City, Countrylanguage tables.')
    except Exception as e:
        connection.rollback()
        print(f'Error inserting data: {e}')

def view_city_country():
    country_code = input('country code:')
    try:
        with connection.cursor() as cursor:
            # Execute queries in seq
            cursor.execute(wq.select_city_country_query(), country_code)
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        connection.rollback()
        print(f'Error inserting data: {e}')
        
def view_country_languege(country_languege_data):
    try:
        with connection.cursor() as cursor:
            # Execute queries in seq
            cursor.execute(wq.select_country_languege(), country_languege_data)
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        connection.rollback()
        print(f'Error inserting data: {e}')
        
def view_population(max, min):
    try:
        with connection.cursor() as cursor:
            # Execute queries in seq
            cursor.execute(wq.select_population(), (min, max))
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Exception as e:
        connection.rollback()
        print(f'Error inserting data: {e}')
        
        
def update_city_country(code,name,population, district):
    try:
        with connection.cursor() as cursor:
            cursor.execute(wq.update_city_country_query(), (population, district, name, code))
            connection.commit()
            print(f'Updated Successful')
    except Exception as e:
        connection.rollback()
        print(f'Error inserting data: {e}')
    finally:
        if cursor:
            cursor.close()
    