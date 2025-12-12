"""
Übung 3: Song mit Listen

Aufgabe:
Erstelle eine Klasse `Song` mit:
- Konstruktor mit Parametern: titel (String) und interpreten (Liste, z.B. ["Artist1", "Artist2"])
- Methode interpret_hinzufuegen(name) mit Parameter:
  - Fügt einen neuen Interpreten zur Liste hinzu
  - Gibt aus "🎤 {name} wurde hinzugefügt"
- Methode zeige_info() ohne Parameter:
  - Zeigt Titel und alle Interpreten an
- Methode anzahl_interpreten() ohne Parameter:
  - Gibt die Anzahl der Interpreten zurück
- Methode play() ohne Parameter:
  - Gibt aus "▶️ Song '{titel}' wird gespielt..."

Erstelle einen Song mit einem Titel und 2 Interpreten deiner Wahl,
zeige die Info, füge einen weiteren Interpreten hinzu, zeige die Anzahl und die Info nochmal.
Spiele dann den Song ab.

💡 Tipps:
- self.interpreten.append(name) fügt ein Element zur Liste hinzu
- len(self.interpreten) gibt die Anzahl der Elemente zurück
- Mit einer for-Schleife kannst du alle Interpreten ausgeben
- Du kannst beliebige Interpreten und Titel verwenden!

Beispiel Ergebnis:
🎵 Song: Summer Vibes
   Interpreten: DJ Max, Sarah Sound
🎤 Beat Producer wurde hinzugefügt
👥 Anzahl Interpreten: 3
🎵 Song: Summer Vibes
   Interpreten: DJ Max, Sarah Sound, Beat Producer
▶️ Song 'Summer Vibes' wird gespielt...
"""

# TODO: Erstelle hier die Klasse Song


# TODO: Erstelle einen Song mit einem Titel und 2 Interpreten deiner Wahl
class Song:
    def __init__(self, titel, interpreten):
        self.titel = titel
        self.interpreten = interpreten

    def interpret_hinzufuegen(self, name):
        self.interpreten.append(name)
        print(f"🎤 {name} wurde hinzugefügt")

    def zeige_info(self):
        print(f"🎵 Song: {self.titel}")
        print("   Interpreten: " + ", ".join(self.interpreten))

    def anzahl_interpreten(self):
        return len(self.interpreten)

    def play(self):
        print(f"▶️ Song '{self.titel}' wird gespielt...")

# TODO: Zeige die Song-Info
mein_song = Song("Summer Vibes", ["DJ Max", "Sarah Sound"])
mein_song.zeige_info()  
mein_song2 = Song("Die with a Smile", ["DBruno Mars", "Lady Gaga"])
mein_song2.zeige_info()   


# TODO: Füge einen weiteren Interpreten hinzu
mein_song.interpret_hinzufuegen("Beat Producer") 


# TODO: Zeige die Anzahl der Interpreten
print(f"👥 Anzahl Interpreten: {mein_song.anzahl_interpreten()}")

# TODO: Zeige die Song-Info erneut
mein_song.zeige_info()  

# TODO: Spiele den Song ab
mein_song.play()  