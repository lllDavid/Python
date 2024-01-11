from mysql.connector import MySQLConnection
from sqlCreate import *

def filtern():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456', 
        port=3307,
        auth_plugin='mysql_native_password',
        database='meinedatenbank'
    )

    mycursor = mydb.cursor()

    suchbegriff = input("Geben Sie einen Suchbegriff ein: ")

    
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
    
