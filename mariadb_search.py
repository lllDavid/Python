import mariadb

def search_db():
    mydb = mariadb.connect(
        host='localhost',
        user='user',
        password='123456', 
        port=3306,
        database="Shop"
    )

    mycursor = mydb.cursor()

    suchbegriff = input("Suchbegriff: ")
    suchen = f"SELECT * FROM kunden WHERE ID LIKE '%{suchbegriff}%' OR LastName LIKE '%{suchbegriff}%' OR FirstName LIKE '%{suchbegriff}%' OR Ort LIKE '%{suchbegriff}%' OR Addresse LIKE '%{suchbegriff}%'"

    mycursor.execute(suchen)
    ergebnisse = mycursor.fetchall()

    if ergebnisse:
        print(f"Ergebnisse für '{suchbegriff}':")
        for e in ergebnisse:
            print(e)
    else:
        print(f"Der Begriff '{suchbegriff}' ist nicht vorhanden!")

    mydb.close()
    
