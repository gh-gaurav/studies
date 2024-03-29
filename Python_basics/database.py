import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='gaurav'
)
cursor = connection.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS faculty(
        fid int primary key,
        fname varchar(40)
    )
     """
#drop_table_query = "DROP TABLE faculty"
#cursor.execute(create_table_query)

insert_query = "INSERT INTO faculty (fid, fname) VALUES(%s, %s)"

faculty_data = [
    (3001,'Nitin Uikey'),
    (3002,'Chaitali Uikey'),
    (3003,'Preeti Saxena'),
    (3004,'Mohit Varma')
]

#cursor.executemany(insert_query,faculty_data)

# connection.commit()
#connection.rollback()
# select_query = "SELECT fname FROM faculty"
# cursor.execute(select_query)

# rows = cursor.fetchall()

# for row in rows:
#     print(row)
cursor.close()
connection.close()