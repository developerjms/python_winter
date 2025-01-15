import os
import book_list as insertall
import book_query_fn as bqf

def menu():
    print('\nbook Database')
    print('''1. 책 추가 2. 모든책보기 3. 책하나찾기 4. 책업데이트 5. 모든회원보기 6. 회원추가 7. 회원한명찾기 
          8.회원업데이트 9.모든주문보기 10. 하나주문보기 11. 주문추가 12.''')
    
    
def book_insert():
    book_insert_data = insertall.collect_book_data()
    bqf.insert_book(book_insert_data=book_insert_data)

def book_selete_all():
 	bqf.view_book_all()

def book_one_select():
    book_no = input('책번호를 입력하세요 : ')
    bqf.view_book(book_no=book_no)

def book_update():
    book_no = input('변경하려는 책 번호를 입력하세요 : ')
    book_type = input('변경하려는 책의 타입을 입력하세요 : ')
    price =  input('변경하려는 책의 가격을 입력하세요 :')
    bqf.update_book(book_no, book_type, price)

def member_select_all():
    bqf.view_member_all()

def member_insert():
    member_insert_data = insertall.collect_member_data()
    bqf.insert_member(member_insert_data=member_insert_data)

def member_one_select():
    member = input('찾으실 회원 번호를 입력하세요 : ')
    bqf.view_member(member=member)

def member_update():
    mem_no = input('변경하시려는 회원번호를 입력하세요 : ')
    mem_addr = input("변경하는 이메일 : ")
    email_id = input('변경하려는 이메일 : ')
    htel_no = input('변경하려는 집전화 번호 : ')
    bqf.update_member(mem_no=mem_no, mem_addr=mem_addr, email_id=email_id, htel_no=htel_no)


def order_select_all():
    bqf.view_order_all()

def order_one_select_book():
    cho = input('1. 주문번호로 책 정보 조회 2. 회원 번호로 주문 정보 조회')
    if cho == '1':
        order_no = input('주문번호를 입력하세요 : ')
        bqf.view_book_order(order_no)
    elif cho == '2':
        pass
    else:
        return
    
    order = input('주문에대한 책 번호를 입력하세요 : ')

def order_insert_bookorder():
    pass

# def order_insert_orderitem():
# 	pass

# def order_insert_delibery():
# 	pass
    

def main():
    try:
        while True:
            menu()
            choice = input('Enter tyour choice : ')
            if choice == '1':
                book_insert()
            elif choice == '2':
                book_selete_all()
            elif choice == '3':
                book_one_select()
            elif choice == '4':
                book_update()
            elif choice == '5':
                member_select_all()
            elif choice == '6':
                member_insert()
            elif choice == '7':
                member_one_select()
            elif choice == '8':
                member_update()
            elif choice == '9':
                order_select_all()
            elif choice == '10':
                #order_one_select_book()
                pass
            elif choice == '11':
                #order_insert_bookorder()
                pass
            elif choice == '12':
                #order_insert_orderitem()
                pass
            elif choice == '13':
                #order_insert_delibery()
                pass
            elif choice == '14':
                os.system('cls')
            elif choice == '15':
                break
            else:
                print('Invalid choice. Please try again.')
    finally:
        print('System closed.')
    
    
if __name__ == "__main__":
    main()