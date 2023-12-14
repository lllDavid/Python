import mariadb

def create():
    mydb = mariadb.connect(
        host='localhost',
        user='david',
        password='12345',
        port=3306,
        
    )
            
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS meinedatenbank")
    mycursor.execute("USE meinedatenbank")
    mycursor.execute("CREATE TABLE IF NOT EXISTS kunden (name VARCHAR(255), ort VARCHAR(255))")
    print("Angelegt!")

    daten = [
        ("Max", "Berlin"),
        ("Anna", "München"),
        ("Peter", "Hamburg"),
        ("Daniel", "Dortmund"),
        ("Sammy","Bremen")
    ]

    einfuegen = "INSERT INTO kunden (name, ort) VALUES (%s, %s)"

    for d in daten:
        mycursor.execute(einfuegen, d)

    mydb.commit()
    mydb.close() 





