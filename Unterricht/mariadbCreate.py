import mariadb

def create():
    mydb = mariadb.connect(
        host='localhost',
        user='david',
        password='12345',
        port=3306,
        
    )
            
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS PythonDB")
    mycursor.execute("USE PythonDB")
    mycursor.execute("CREATE TABLE IF NOT EXISTS kunden (id INTEGER, name VARCHAR(255), ort VARCHAR(255), age INTEGER)")
    print("Angelegt!")

    daten = [
        (1,"Max", "Berlin",22),
        (2,"Anna", "München",23),
        (3,"Peter", "Hamburg",24),
        (4,"Daniel", "Dortmund",25),
        (5,"Sammy","Bremen",26)
    ]

    einfuegen = "INSERT INTO kunden (id, name, ort, age) VALUES (%s,%s, %s,%s)"

    for d in daten:
        mycursor.execute(einfuegen, d)

    mydb.commit()
    mydb.close() 





