movie_1 = ["Horror","It", 2017, 135]
movie_2 = ["Fantasy","Harry Potter", 1997, 97]

print(f"Titel des Films: {movie_1[1]}")
print(f"Titel des Films: {movie_2[1]}")

class Movie: #Klasse= Bauplan für unseren Thema
    def __init__(self, title, genre, duration, release_year): #Konstuktor -> wird immer aufgerufen
        #wenn ein neus Objekt erstellt wird
        self.title = title
        self.genre = genre
        self.duration = duration
        self.realease_year = release_year
        print("Neuer Film wurde erstellt")

# movie_3 = Movie()  #erstellt uns ein objekt nach dem Bauplan "Movie"
# movie_4 = Movie() 
# movie_5 = Movie() 

# movie_3.title = "Real Steal"
# print(f"Title des Filmes: {movie_3.title}")

# movie_3.genre = "Action"
# movie_3.duration = 1120
# movie_3.release_year = 2015

# movie_4.title = "Barbie Fairytopia"
# print(f"Title des Filmes: {movie_4.title}")

# movie_4.genre = "Action"
# movie_4.duration = 140
# movie_4.release_year = 2004

movie_6 = Movie(title ="Dune: Awakening", genre="Sci-Di", duration=180,release_year=2020)
print(f"Title des Filmes: {movie_6.title}")

movie_7 = Movie(title ="Barbie", genre="Drama", duration=125,release_year=2023)
print(f"Title des Filmes: {movie_7.title} wurde im Jahr {movie_7.realease_year} herrausgebracht!")

