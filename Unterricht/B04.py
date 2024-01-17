eingabe = "Was geht am Wochenende?"
 
if eingabe == "Was geht am Wochenende?":
    text = open("C:\\Users\David\Documents\Workspace\Python\Übungen\maxundmoritz.txt", "r", encoding="utf-8")
    for t in text:
        if "Menschen necken, Tiere quälen," in t or "Äpfel, Birnen, Zwetschen stehlen" in t:
            print(t)
 
text = open("C:\\Users\David\Documents\Workspace\Python\Übungen\maxundmoritz.txt", "a", encoding="utf-8")
text.write("Hinzugefügter Text")
text.close()

text = open("C:\\Users\David\Documents\Workspace\Python\Übungen\maxundmoritz.txt", "r", encoding="utf-8")
print(text.read())
text.close()

text = open("C:\\Users\David\Documents\Workspace\Python\Übungen\maxundmoritz.txt", "w")
text.write("Oh-Oh! Ich habe den Inhalt gelöscht!")
text.close()

text = open("C:\\Users\David\Documents\Workspace\Python\Übungen\maxundmoritz.txt", "r")
print(text.read())