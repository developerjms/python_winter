import os
import world_insert_all as insertall
import world_query_fn as wqf

def menu():
    print('\nWorld Database')
    print('1. Insert City 2. Update city 3. Delete City 4. View Cities 5. Clear 6. Exit 7. Insert All')
    
def insert_world():
    country_data = insertall.collect_country_data() # country data input (return tuple)
    city_data = insertall.collect_city_data()       # city data input (return tuple)
    # 디비에 연동하는 코드.
    wqf.insert_city_country(country_data=country_data, city_data=city_data)

def insert_date_all():
    country_data = insertall.collect_country_data() # country data input (return tuple)
    city_data = insertall.collect_city_data()       # city data input (return tuple)
    country_language_data = insertall.collect_country_language_data()
    # 디비에 연동하는 코드.
    wqf.insert_all(country_data=country_data, city_data=city_data, country_language_data=country_language_data)

def select_world():
    cho = input('1. city_country(code) 2. country_languege(code, name) 3. population(between) : ')
    if cho == '1':
        wqf.view_city_country()
    elif cho == '2':
        country_languege_data=insertall.collect_country_languege_date()
        wqf.view_country_languege(country_languege_data=country_languege_data)
    elif cho == '3':
        min = int(input('최소값: '))
        max = int(input('최대값:'))
        wqf.view_population(max=max, min=min)
def update_world():
    name = input('Enter city name:')
    country_code = input("Enter city country_code:")
    district = input("Enter city district:")
    population = int(input('Enter city population: '))
    wqf.update_city_country(population=population, district=district, name=name, code=country_code)
def main():
    try:
        while True:
            menu()
            choice = input('Enter tyour choice : ')
            if choice == '1':
                insert_world()
            elif choice == '2':
                update_world()
            elif choice == '3':
                #delete_world()
                pass
            elif choice == '4':
                select_world()
            elif choice == '5':
                os.system('cls')
            elif choice == '6':
                break
            elif choice == '7':
                insert_date_all()
            else:
                print('Invalid choice. Please try again.')
    finally:
        print('System closed.')
    
    
if __name__ == "__main__":
    main()