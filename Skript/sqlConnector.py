import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',    ### Passwort eingeben
    port = 3307,                ### Standard 3306
    auth_plugin='mysql_native_password'
)

cursor = conn.cursor()
 
database_name = 'BeispielDatenbank'
create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
cursor.execute(create_database_query)

print(f"Datenbank '{database_name}' angelegt!")


conn.database = database_name

create_table_query = '''
    CREATE TABLE IF NOT EXISTS your_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
'''
cursor.execute(create_table_query)


data_to_insert = [
    ("David", 26),
    ("Daniel", 24),
    ("Tom", 20)
]

insert_query = "INSERT INTO your_table (name, age) VALUES (%s, %s)"

for record in data_to_insert:
    cursor.execute(insert_query, record)

conn.commit()
conn.close()

print("Datenbank,Tabellen und Datein hinzugefügt!")

