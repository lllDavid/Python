import os
eingabe = input("Wollen sie den Ordner löschen ? Ja/Nein: ")
if eingabe == "Ja":
    os.remove("C:\\Users\\David\Documents\\Workspace\\Python\\Testordner\\text1.txt")
    os.remove("C:\\Users\\David\Documents\\Workspace\\Python\\Testordner\\text2.txt")
    os.remove("C:\\Users\\David\Documents\\Workspace\\Python\\Testordner\\text3.txt")
    os.rmdir("C:\\Users\\David\Documents\\Workspace\\Python\\Testordner")
else:
    print("Nichts gelöscht")
