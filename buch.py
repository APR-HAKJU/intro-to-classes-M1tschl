# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:


- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""

# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.
class Buch:
    def __init__(self , title, autor, gelesen):
        self.title = title
        self.autor = autor
        self.gelesen = gelesen
        print ("neues Buch wurde hinzugefügt")
    
Buch_1 = Buch(title = "Harry potter", autor= "JK Rowling", gelesen= True)
Buch_2 = Buch(title = "Mein Kampf", autor="A.H.", gelesen= False)
Buch_2 = Buch(title = "Die drei Fragezeichen" , autor="Horsti" ,gelesen= False)

