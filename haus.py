# TODO: Aufgabe 1:
# Ändere den Code unten, so dass die Eigenschaften des Hauses als Attribute im Konstruktor definiert sind.
# Aktuell werden die Eigenschaften als separate Variablen definiert.
# Definiere einen Konstruktor (__init__), um die Attribute zu initialisieren.
class Haus1:
    def __init__(self, quadratmeter, schlafzimmer, badezimmer):
        self.quadratmeter = quadratmeter
        self.schlafzimmer = schlafzimmer
        self.badezimmer = badezimmer

haus1 = Haus1(120, 3, 2) #haus1


print(f"Haus1: {haus1.quadratmeter}m², {haus1.schlafzimmer} Schlafzimmer, {haus1.badezimmer} Badezimmer")

# TODO: Aufgabe 2: Erstelle drei weitere Objekte der Klasse Haus mit unterschiedlichen Eigenschaften.

class Haus2:
    def __init__(self, quadratmeter, schlafzimmer, badezimmer):
        self.quadratmeter = quadratmeter
        self.schlafzimmer = schlafzimmer
        self.badezimmer = badezimmer

haus2 = Haus2(100, 2, 1)


class Haus3:
    def __init__(self, quadratmeter, schlafzimmer, badezimmer):
        self.quadratmeter = quadratmeter
        self.schlafzimmer = schlafzimmer
        self.badezimmer = badezimmer

haus3 = Haus3(90, 1, 1)

class Haus4:
    def __init__(self, quadratmeter, schlafzimmer, badezimmer):
        self.quadratmeter = quadratmeter
        self.schlafzimmer = schlafzimmer
        self.badezimmer = badezimmer

haus4 = Haus4(185, 4, 3)


# TODO: Aufgabe 3: Gib die Anzahl der Schlafzimmer und Badezimmer für jedes Haus aus.

print(f"Haus1: {haus1.quadratmeter}m², {haus1.schlafzimmer} Schlafzimmer, {haus1.badezimmer} Badezimmer")
print(f"Haus2: {haus2.quadratmeter}m², {haus2.schlafzimmer} Schlafzimmer, {haus2.badezimmer} Badezimmer")
print(f"Haus3: {haus3.quadratmeter}m², {haus3.schlafzimmer} Schlafzimmer, {haus3.badezimmer} Badezimmer")
print(f"Haus4: {haus4.quadratmeter}m², {haus4.schlafzimmer} Schlafzimmer, {haus4.badezimmer} Badezimmer")