"""
Übung 1: Auto-Klasse mit Methoden

Aufgabe:
Erstelle eine Klasse `Auto` mit:
- Konstruktor mit Parametern: marke, modell, kilometerstand
- Methode(funtion in einer Klasse) fahren() ohne Parameter: Erhöht den Kilometerstand um 100
  und gibt aus: "Gefahren! Neuer Stand: X km"
- Methode zeige_info() ohne Parameter: Gibt Marke, Modell und 
  Kilometerstand aus

Erstelle ein Auto und lass es dreimal fahren.
"""
class auto:
    def __init__(self, marke, modell, kilometerstand):
        self.marke = marke
        self.modell = modell
        self.kilometerstand = kilometerstand

    def fahren(self):
        self.kilometerstand += 100
        print(f"Gefahren! Neuer Stand: {self.kilometerstand} km")

    def zeige_info(self):
        print(f"{self.marke} {self.modell}, Kilometerstand: {self.kilometerstand} km")
"""
💡 Tipp:
- In fahren() verwendest du self.kilometerstand += 100
- Denke daran, dass Methoden immer self als ersten Parameter haben!

Erwartetes Ergebnis:
VW Golf, Kilometerstand: 50000 km
Gefahren! Neuer Stand: 50100 km
Gefahren! Neuer Stand: 50200 km
Gefahren! Neuer Stand: 50300 km
VW Golf, Kilometerstand: 50300 km
"""

# TODO: Erstelle hier die Klasse Auto
class Auto:
    def __init__(self, marke, modell, kilometerstand):
        self.marke = marke
        self.modell = modell
        self.kilometerstand = kilometerstand
    def fahren(self):
        self.kilometerstand += 100
        print(f"Gefahren! Neuer Stand: {self.kilometerstand} km")

    def zeige_info(self):
        print(f"{self.marke} {self.modell}, Kilometerstand: {self.kilometerstand} km")
# TODO: Erstelle ein Auto-Objekt (z.B. VW Golf mit 50000 km)
auto1 = Auto("VW", "Golf", 50000)
print(f"{auto1.marke} {auto1.modell}, Kilometerstand: {auto1.kilometerstand} km")

# TODO: Zeige die Info
auto1.zeige_info()

# TODO: Lass das Auto dreimal fahren
auto1.fahren()
auto1.fahren() 
auto1.fahren()

# TODO: Zeige die Info erneut
auto1.zeige_info()