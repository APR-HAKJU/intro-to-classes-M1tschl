"""
Übung 2: Kaffeemaschine mit Parametern

Aufgabe:
Erstelle eine Klasse `Kaffeemaschine` mit:
- Konstruktor mit Parameter: wasserstand (in ml, z.B. 1000)
- Methode kaffee_machen(menge) mit Parameter:
  - Prüft, ob genug Wasser da ist
  - Wenn ja: Reduziert Wasserstand und gibt aus "☕ Kaffee gemacht! X ml"
  - Wenn nein: Gibt aus "❌ Nicht genug Wasser! Bitte nachfüllen."
- Methode wasser_nachfuellen(menge) mit Parameter: Erhöht den Wasserstand
- Methode zeige_status() ohne Parameter: Zeigt aktuellen Wasserstand

Erstelle eine Kaffeemaschine mit 500ml Wasser, mache 2x Kaffee (je 200ml),
versuche es nochmal (es sollte dieses Mal fehlschlagen), fülle Wasser nach und mache nochmal Kaffee.

💡 Tipps:
- Verwende if self.wasserstand >= menge: um zu prüfen
- self.wasserstand -= menge verringert den Wasserstand
- self.wasserstand += menge erhöht den Wasserstand

Erwartetes Ergebnis:
Wasserstand: 500 ml
☕ Kaffee gemacht! 200 ml
☕ Kaffee gemacht! 200 ml
❌ Nicht genug Wasser! Bitte nachfüllen.
💧 500 ml Wasser nachgefüllt
☕ Kaffee gemacht! 200 ml
Wasserstand: 400 ml
"""

# TODO: Erstelle hier die Klasse Kaffeemaschine
class Kaffeemaschine:
    def __init__(self, wasserstand):
        self.wasserstand = wasserstand

    def kaffee_machen(self, menge):
        if self.wasserstand >= menge:
            self.wasserstand -= menge
            print(f"Kaffee gemacht! {menge} ml")
        else:
            print("Nicht genug Wasser! Bitte nachfüllen.")

    def wasser_nachfuellen(self, menge):
        self.wasserstand += menge
        print(f"{menge} ml Wasser nachgefüllt")

    def zeige_status(self):
        print(f"Wasserstand: {self.wasserstand} ml")

# TODO: Erstelle eine Kaffeemaschine mit 500ml Wasser
maschine = Kaffeemaschine(500)

# TODO: Zeige den Status
maschine.zeige_status()

# TODO: Mache 2x Kaffee mit je 200ml
maschine.kaffee_machen(200)
maschine.kaffee_machen(200)   

# TODO: Versuche nochmal Kaffee zu machen (sollte fehlschlagen)
maschine.kaffee_machen(200)

# TODO: Fülle 500ml Wasser nach
maschine.wasser_nachfuellen(500)

# TODO: Mache nochmal Kaffee mit 200ml
maschine.kaffee_machen(200)

# TODO: Zeige den Status erneut 
maschine.zeige_status()     