import mysql.connector
from mysql.connector import Error

def create_connection(host_name,user_name,user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )
        print("connection is established successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_database(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("Databse is created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()        
def use_database(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("You are now using the database")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
    
def create_table(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("table is created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close() 

def insert_table(connection,query,data):
    try:
        cursor = connection.cursor()
        cursor.executemany(query,data)
        connection.commit()
        print("insertion into table is successfully")
    except Error as e:
        print(f"The error '{e}' occurred")        
    finally:
        cursor.close()
        
def select_table(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print("This is the data from your table:")
        for row in rows:
            print(row) 
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()    
          
    
create_database_query = "CREATE DATABASE IF NOT EXISTS gaurav2"
use_database_query ="USE gaurav2"
create_table_query = """
    CREATE TABLE IF NOT EXISTS customer(
        cid int primary key,
        cname varchar(40)
    )
    """
insert_query = "INSERT INTO customer values(%s, %s)"
customer_data = [
    (201,"Gaurav"),
    (202,"Sakshi"),
    (203,"Priya"),
    (204,"Pranjal"),
    (205,"Mayur"),
    (206,"Shivam")
]
select_query = "SELECT * FROM customer"

try:
    connection = create_connection('localhost','root','admin')
    create_database(connection,create_database_query)
    use_database(connection,use_database_query)
    create_table(connection,create_table_query)
    insert_table(connection,insert_query,customer_data)
    select_table(connection,select_query)
except Error as e:
    print(f"The error '{e}' occurred")
finally:
    if connection:
        connection.close()
        print("connection is now closed")