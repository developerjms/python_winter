def book_insert_sql():
    sql = """INSERT INTO BOOK(BOOK_NO, BOOK_NM, BOOK_TYPE, QTY, SUP_PRICE, AUTHOR, PUB_DATE, PRICE, APPLY_DISCOUNT_RATE, STOCK_QTY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    return sql

def book_select_sql():
    sql = """SELECT * FROM BOOK"""
    return sql

def book_select_sql_1():
    sql = "SELECT * FROM BOOK WHERE BOOK_NO=%s"
    return sql

def book_update_sql():
    sql = """UPDATE BOOK SET BOOK_TYPE = %s, PRICE = %s WHERE BOOK_NO = %s"""
    return sql

def member_select_sql():
    sql = """SELECT * FROM MEMBER"""
    return sql

def member_insert_sql():
    sql = """INSERT INTO MEMBER(MEMBER_NO, JUMIN_NO, MEMBER_ADDR, MEMBER_TEL, EMAIL_ID, MEMBER_HTEL_NO, SIGNMETHOD_CD, BUY_POINT)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    return sql

def member_select_sql_1():
    sql = """SELECT * FROM MEMBER WHERE MEMBER_NO=%s"""
    return sql

def member_update_sql():
    sql = "UPDATE MEMBER SET MEMBER_ADDR = %s, EMAIL_ID = %s, MEMBER_HTEL_NO = %s WHERE MEMBER_NO = %s"
    return sql

def order_select_sql():
    # sql = """SELECT o.ORDER_NO, o.MEMBER_NO, o.DELIVERY_NO, o.DELIVERY_PLACE, o.ORDER_DATE, o.EL
    #          FROM bookorder as o, orderitem as oi, delivery as d
    #          WHERE o.order_no = oi.order_no
    #          AND d.delivery_no = o.delivery_no"""
    sql = """
        SELECT bo.ORDER_NO, bo.MEMBER_NO, bo.DELIVERY_NO, bo.DELIVERY_PLACE, bo.ORDER_DATE, bo.EL
        FROM bookorder as bo, orderitem as oi, delivery as d
        WHERE bo.order_no = oi.order_no
        AND d.delivery_no = bo.delivery_no;
    """
    return sql

def order_select_book_sql():
    sql = "SELECT * FROM BOOK where book_type=%s"
    return sql

def order_insert_bookorder_sql():
    sql = """INSERT INTO BOOKORDER(ORDER_NO, MEMBER_NO, DELIVERY_NO, DELIVERY_PLACE, ORDER_DATE, EL)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    return sql

def order_insert_orderitem_sql():
    sql = """INSERT INTO ORDERITEM(BOOK_NO, ORDER_NO, CNT) VALUES (%s, %s, %s)"""
    return sql

def order_insert_delivery_sql():
    sql = """INSERT INTO DELIVERY(DELIVERY_NO, DELIVERY_DATE, DELIVERY_CD, DELIVERRSLT_CD) VALUES (%s, %s, %s, %s)"""
    return sql