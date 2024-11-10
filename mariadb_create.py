import mariadb

def create_db():
    mydb = mariadb.connect(
        host='localhost',
        user='user',
        password='123456',
        port=3306,
    )
            
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS Shop")
    mycursor.execute("USE Shop")
    mycursor.execute("CREATE TABLE IF NOT EXISTS kunden (ID INTEGER PRIMARY KEY, LastName VARCHAR(255), FirstName VARCHAR(255), Ort VARCHAR(255), Addresse VARCHAR(255))")
    print("Datenbank angelegt!")

    daten = [
        (1,"Meier", "Max", "Berlin", "Berlin-Straße 42"),
        (2,"Müller", "Anna", "München", "Münchnerweg 23"),
        (3,"Musterman", "Peter", "Hamburg", "Hamburger Allee 12c"),
        (4,"Lehner", "Alex", "Dortmund", "Dortmund Straße 34"),
        (5,"Hansen", "Markus","Bremen", "Bremenweg 32d"),
        (6,"Werter", "Hans","Rosenheim", "Rosenheimer Straße 23d")
    ]

    einfuegen = "INSERT INTO kunden (ID, LastName, FirstName, Ort, Addresse) VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE ID=ID"  

    for d in daten:
        mycursor.execute(einfuegen, d)

    mydb.commit()
    mydb.close() 





