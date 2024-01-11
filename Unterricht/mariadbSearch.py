import mariadb


def search():
    mydb = mariadb.connect(
        host='localhost',
        user='david',
        password='123456', 
        port=3306,
        database="PythonDB"
        
    )

    mycursor = mydb.cursor()

    suchbegriff = input("Suchen: ")

    
    suchen = f"SELECT * FROM kunden WHERE ID LIKE '%{suchbegriff}%' OR Name LIKE '%{suchbegriff}%' OR Ort LIKE '%{suchbegriff}%' OR notAlter LIKE '%{suchbegriff}%'"

    mycursor.execute(suchen)
    ergebnisse = mycursor.fetchall()

    if ergebnisse:
        print(f"Ergebnisse für '{suchbegriff}':")
        for e in ergebnisse:
            print(e)
    else:
        print(f"Der Begriff '{suchbegriff}' ist nicht vorhanden!")

    mydb.close()
    
