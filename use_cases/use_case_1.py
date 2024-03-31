import json
from datetime import datetime
import mysql.connector

#open file
f =  open('training_session.json', 'r')

# Reading data from json file
training_data = json.load(f)

#closing the file
f.close()
 
#extracting information from json data    
training_name = training_data['name']
training_date_str = training_data['date']
training_date = datetime.strptime(training_date_str, '%B %d, %Y').strftime('%Y-%m-%d')
training_completed = training_data['completed']
instructor_name = training_data['instructor']['name']
instructor_website = training_data['instructor']['website']
participants = training_data['participants']


#creating connection for mysql database
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'gaurav'
)
cursor = connection.cursor()

#creating table for storing the extracted information
create_table_query_training = '''
    CREATE TABLE IF NOT EXISTS training_session (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        date DATE,
        completed BOOLEAN,
        instructor_name VARCHAR(255),
        instructor_website VARCHAR(255)
    )
'''

create_table_query_participants = '''
    CREATE TABLE IF NOT EXISTS participants (
        id INT AUTO_INCREMENT PRIMARY KEY,
        training_session_id INT,
        name VARCHAR(255),
        email VARCHAR(255),
        FOREIGN KEY (training_session_id) REFERENCES training_session(id)
    )
'''

cursor.execute(create_table_query_training)
cursor.execute(create_table_query_participants)




insert_training_query = '''
    INSERT INTO training_session (name,date,completed,instructor_name,instructor_website)
        VALUES(%s, %s, %s, %s, %s)
    '''

training_session_data = [
    training_name,
    training_date,
    training_completed,
    instructor_name,
    instructor_website
]

#executing the insert into training session
cursor.execute(insert_training_query,training_session_data)

training_session_id = cursor.lastrowid

insert_participants_query = '''
    INSERT INTO participants (training_session_id, name, email)
        VALUES(%s, %s, %s)
'''
for participant in participants:
     cursor.execute(insert_participants_query,(training_session_id, participant['name'], participant['email']))    
    
connection.commit()
connection.close() 

print("Training session data successfully stored in the database.")   
    
    