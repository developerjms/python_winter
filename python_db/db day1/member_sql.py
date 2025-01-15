# def select_member_query():
#     sql = """sql_SELECT = "SELECT * FROM """
#     return sql

def select_member_query():
    return """SELECT * FROM member 
            WHERE delyn='n';"""

def select_member_query_del():
    return """SELECT * FROM member 
            WHERE delyn='y';"""
    
    
def select_member_one_query():
    return """SELECT * FROM member 
            WHERE name=%s"""

def update_member_query():
    return """UPDATE member SET email=%s, age=%s 
            WHERE name=%s"""

def insert_member_query():
    return """INSERT INTO MEMBER (name, email, age, delyn) 
            VALUES (%s, %s, %s, 'n')"""
            
# def delete_member_query():
#     return """DELETE FROM member 
#             WHERE name=%s"""
            
def delete_member_query_y():
    return """UPDATE member SET delyn = 'y' 
            WHERE (mem_no = %s);"""

def delete_member_query_n():
    return """UPDATE member SET delyn = 'n' 
            WHERE (mem_no = %s);"""
            

