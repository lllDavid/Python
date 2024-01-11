import mysql.connector

def erstellen():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        port=3307,
        auth_plugin='mysql_native_password'
    )
            
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS meinedatenbank")
    mycursor.execute("USE meinedatenbank")
    mycursor.execute("CREATE TABLE IF NOT EXISTS kunden (name VARCHAR(255), ort VARCHAR(255))")
    print("Angelegt!")

    daten = [
        ("Max", "Berlin"),
        ("Anna", "München"),
        ("Peter", "Hamburg")
    ]

    einfuegen = "INSERT INTO kunden (name, ort) VALUES (%s, %s)"

    for d in daten:
        mycursor.execute(einfuegen, d)

    mydb.commit()
    mydb.close() 





