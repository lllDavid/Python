import mariadb


def search():
    mydb = mariadb.connect(
        host='localhost',
        user='david',
        password='12345', 
        port=3306,
        database="meinedatenbank"
        
    )

    mycursor = mydb.cursor()

    suchbegriff = input("Suchen: ")

    
    suchen = f"SELECT * FROM kunden WHERE name LIKE '%{suchbegriff}%' OR ort LIKE '%{suchbegriff}%'"

    mycursor.execute(suchen)
    ergebnisse = mycursor.fetchall()

    if ergebnisse:
        print(f"Ergebnisse für '{suchbegriff}':")
        for e in ergebnisse:
            print(e)
    else:
        print(f"Der Begriff '{suchbegriff}' ist nicht vorhanden!")

    mydb.close()
    
