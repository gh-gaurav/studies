import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'gaurav'
)

cursor = connection.cursor()

create_query = """
        CREATE TABLE subject(
            sid int primary key,
            sname varchar(40)
        )
"""
# cursor.execute(create_query)

insert_query = "INSERT INTO subject values(%s, %s)"
subject_data = [
    (201, "Data Structure"),
    (202, "Computer Network"),
    (203, "Operating System"),
    (204, "DBMS"),
]


# cursor.executemany(insert_query,subject_data)
# connection.commit()
select_query = "SELECT * FROM subject"

cursor.execute(select_query)

rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()
connection.close()