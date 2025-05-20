# Liste der Filme (Beispiel)
"""Aufbau:
{
    "title":    Titel:      str
    "rating":   Bewertung:  float 0 - 10 
    "year":     Jahr:       int
    "genres":   Genres:     set(str, [str])
}
"""
movie_list = [
  {"title": "I'm Still Here", "rating": 8.9, "year": 2024, "genres": {"Docudrama", "Period Drama", "Political Drama", "Biography", "Drama", "History"}},
  {"title": "The Substance", "rating": 7.3, "year": 2024, "genres": {"Body Horror", "Dark Comedy", "Monster Horror", "Psychological Horror", "Showbiz Drama", "Drama", "Horror", "Sci-Fi"}},
  {"title": "Alien", "rating": 8.5, "year": 1979, "genres": {"Cyberpunk", "Monster Horror", "Space Sci-Fi", "Horror", "Sci-Fi"}},
  {"title": "Aliens", "rating": 8.4, "year": 1986, "genres": {"Alien Invasion", "Cyberpunk", "Monster Horror", "Space Sci-Fi", "Tragedy", "Action", "Adventure", "Horror", "Sci-Fi", "Thriller"}},
  {"title": "Back to the Future", "rating": 8.5, "year": 1985, "genres": {"High-Concept Comedy", "Teen Adventure", "Time Travel", "Urban Adventure", "Adventure", "Comedy", "Sci-Fi"}},
  {"title": "Inception", "rating": 8.8, "year": 2010, "genres": {"Action Epic", "Adventure Epic", "Epic", "Psychological Thriller", "Sci-Fi Epic", "Action", "Adventure", "Sci-Fi", "Thriller"}},
  {"title": "Interstellar", "rating": 8.7, "year": 2014, "genres": {"Adventure Epic", "Epic", "Quest", "Sci-Fi Epic", "Space Sci-Fi", "Time Travel", "Acventure", "Drama", "Sci-Fi"}},
  {"title": "The Matrix", "rating": 8.7, "year": 1999, "genres": {"Action Epic", "Artificial Intelligence", "Cyberpunk", "Dystopian Sci-Fi", "Gun Fu", "Martial Arts", "Sci-Fi Epic", "Action", "Sci-Fi"}},
  {"title": "Star Wars: Episode IV - A New Hope", "rating": 8.6, "year": 1977, "genres": {"Action Epic", "Adventure Epic", "Epic", "Fantasy Epic", "Quest", "Sci-Fi Epic", "Space Sci-Fi", "Sword & Sorcery", "Action", "Adventure"}},
  {"title": "Star Wars: Episode V - The Empire Strikes Back", "rating": 8.7, "year": 1980, "genres": {"Action Epic", "Adventure Epic", "Dark Fantasy", "Epic", "Fantasy Epic", "Globetrotting Adventure", "Quest", "Sci-Fi Epic", "Space Sci-Fi", "Sword & Sorcery"}},
  {"title": "Star Wars: Episode VI - Return of the Jedi", "rating": 8.3, "year": 1983, "genres": {"Action Epic", "Adventure Epic", "Dark Fantasy", "Epic", "Fantasy Epic", "Globetrotting Adventure", "Quest", "Sci-Fi Epic", "Space Sci-Fi", "Sword & Sorcery"}},
  {"title": "The NeverEnding Story", "rating": 7.3, "year": 1984, "genres": {"Adventure Epic", "Fantasy Epic", "Quest", "Sword & Sorcery", "Adventure", "Drama", "Family", "Fantasy"}},
  {"title": "The Lord of the Rings: The Fellowship of the Ring", "rating": 8.9, "year": 2001, "genres": {"Action Epic", "Adventure Epic", "Epic", "Fantasy Epic", "Quest", "Sword & Sorcery", "Adventure", "Drama", "Fantasy"}},
  {"title": "The Lord of the Rings: The Two Towers", "rating": 8.8, "year": 2002, "genres": {"Action Epic", "Adventure Epic", "Dark Fantasy", "Epic", "Fantasy Epic", "Quest", "Sword & Sorcery", "Adventure", "Drama", "Fantasy"}},
  {"title": "The Lord of the Rings: The Return of the King", "rating": 9.0, "year": 2003, "genres": {"Action Epic", "Adventure Epic", "Epic", "Fantasy Epic", "Mountain Adventure", "Quest", "Sword & Sorcery", "Tragedy", "Adventure", "Drama"}},
  {"title": "Raiders of the Lost Ark", "rating": 8.4, "year": 1981, "genres": {"Adventure Epic", "Desert Adventure", "Globetrotting Adventure", "Quest", "Action", "Adventure"}},
  {"title": "Indiana Jones and the Temple of Doom", "rating": 7.5, "year": 1984, "genres": {"Adventure Epic", "Globetrotting Adventure", "Jungle Adventure", "Action", "Adventure"}},
  {"title": "Indiana Jones and the Last Crusade", "rating": 8.2, "year": 1989, "genres": {"Adventure Epic", "Desert Adventure", "Globetrotting Adventure", "Quest", "Action", "Adventure"}},
  {"title": "Up", "rating": 8.3, "year": 2009, "genres": {"Coming-of-Age", "Computer Animation", "Globetrotting Adventure", "Adventure", "Animation", "Comedy", "Drama", "Family"}},
  {"title": "Se7en", "rating": 8.6, "year": 1995, "genres": {"Cop Drama", "Hard-boiled Detective", "Legal Drama", "Police Procedural", "Psychological Thriller", "Serial Killer", "Crime", "Drama", "Mystery", "Thriller"}},
  {"title": "The Silence of the Lambs", "rating": 8.6, "year": 1991, "genres": {"Police Procedural", "Psychological Drama", "Psychological Thriller", "Serial Killer", "Crime", "Drama", "Thriller"}},
  {"title": "Memento", "rating": 8.4, "year": 2000, "genres": {"Psychological Thriller", "Suspense Mystery", "Mystery", "Thriller", "", "", "", "", "", ""}},
  {"title": "Donnie Darko", "rating": 8.0, "year": 2001, "genres": {"Psychological Drama", "Psychological Thriller", "Time Travel", "Drama", "Mystery", "Sci-Fi", "Thriller"}},
  {"title": "Primer", "rating": 6.7, "year": 2004, "genres": {"Time Travel", "Drama", "Sci-Fi", "Thriller"}},
  {"title": "M - Eine Stadt sucht einen Mörder", "rating": 8.3, "year": 1931, "genres": {"Psychological Thriller", "Serial Killer", "Suspense Mystery", "Crime", "Mystery", "Thriller"}},
  {"title": "Black Swan", "rating": 8.0, "year": 2010, "genres": {"Psychological Drama", "Psychological Thriller", "Showbiz Drama", "Drama", "Thriller"}},
  {"title": "Perfect Blue", "rating": 8.0, "year": 1997, "genres": {"Adult Animation", "Anime", "Dop Drama", "Erotic Thriller", "Hand-Drawn Animation", "Hard-boiled Detective", "Legal Drama", "Legal Thriller", "Police Procedural", "Psychological Thriller"}},
  {"title": "Blade Runner", "rating": 8.1, "year": 1982, "genres": {"Artificial Intelligence", "Cyber Thriller", "Cyberpunk", "Dystopian Sci-Fi", "Action", "Drama", "Sci-Fi", "Thriller"}},
  {"title": "Blade Runner 2049", "rating": 8.0, "year": 2017, "genres": {"Action Epic", "Artificial Intelligence", "Cyber Thriller", "Cyberpunk", "Dystopian Sci-Fi", "Epic", "Sci-Fi Epic", "Action", "Drama", "Mystery"}},
  {"title": "Her", "rating": 8.0, "year": 2013, "genres": {"Artificial Intelligence", "Drama", "Romance", "Sci-Fi"}},
  {"title": "2001: A Space Odyssey", "rating": 8.3, "year": 1968, "genres": {"Adventure Epic", "Artificial Intelligence", "Epic", "Psychological Drama", "Sci-Fi Epic", "Space Sci-Fi", "Adventure", "Sci-Fi"}},
  {"title": "Akira", "rating": 8.0, "year": 1988, "genres": {"Action Epic", "Adult Animation", "Anime", "Cyberpunk", "Dark Fantasy", "Dystopian Sci-Fi", "Epic", "Fantasy Epic", "Hand-Drawn Animation", "Political Drama"}},
  {"title": "Metropolis", "rating": 8.3, "year": 1927, "genres": {"Dystopian Sci-Fi", "Epic", "Sci-Fi Epic", "Steampunk", "Drama", "Sci-Fi"}},
  {"title": "Poor Things", "rating": 7.8, "year": 2023, "genres": {"Dark Comedy", "Steampunk", "Comedy", "Drama", "Romance", "Sci-Fi"}},
  {"title": "The Prestige", "rating": 8.5, "year": 2006, "genres": {"Period Drama", "Steampunk", "Tragedy", "Drama", "Mystery", "Sci-Fi", "Thriller"}},
  {"title": "Deadpool", "rating": 8.0, "year": 2016, "genres": {"Dark Comedy", "Gun Fu", "Raunchy Comedy", "Superhero", "Action", "Comedy"}},
  {"title": "John Wick", "rating": 7.4, "year": 2014, "genres": {"Gun Fu", "One-Person Army Action", "Action", "Crime", "Thriller"}},
  {"title": "Oldboy", "rating": 8.3, "year": 2003, "genres": {"Dark Comedy", "One-Person Army Action", "Psychological Drama", "Psychological Thriller", "Action", "Drama", "Mystery", "Thriller"}},
  {"title": "Léon: The Professional", "rating": 8.5, "year": 1994, "genres": {"Gangster", "One-Person Army Action", "Action", "Crime", "Drama", "Thriller"}},
  {"title": "Kill Bill: Vol. 1", "rating": 8.2, "year": 2003, "genres": {"Martial Arts", "One-Person Army Action", "Action", "Crime", "Thriller"}},
  {"title": "Die Hard", "rating": 8.2, "year": 1988, "genres": {"Disaster", "One-Person Army Action", "Action", "Holiday", "Thriller"}},
  {"title": "For a Few Dollars More", "rating": 8.2, "year": 1965, "genres": {"One-Person Army Action", "Spaghetti Western", "Drama", "Western"}},
  {"title": "Mulan", "rating": 7.7, "year": 1998, "genres": {"Coming-of-Age", "Hand-Drawn Animation", "Martial Arts", "Period Drama", "Pop Musical", "Adventure", "Animation", "Comedy", "Family", "Fantasy"}},
  {"title": "Gravity", "rating": 7.7, "year": 2013, "genres": {"Disaster", "Sci-Fi Epic", "Space Sci-Fi", "Survival", "Drama", "Sci-Fi", "Thriller"}},
  {"title": "Django Unchained", "rating": 8.5, "year": 2012, "genres": {"Dark Comedy", "Epic", "Period Drama", "Western Epic", "Comedy", "Drama", "Western"}},
  {"title": "The Good, the Bad and the Ugly", "rating": 8.8, "year": 1966, "genres": {"Adventure Epic", "Dark Comedy", "Desert Adventure", "Epic", "Period Drama", "Quest", "Spaghetti Western", "Western Epic", "Adventure", "Drama"}},
  {"title": "A Fistful of Dollars", "rating": 7.9, "year": 1964, "genres": {"Spaghetti Western", "Drama", "Western"}},
  {"title": "The Godfather", "rating": 9.2, "year": 1972, "genres": {"Epic", "Gangster", "Tragedy", "Crime", "Drama"}},
  {"title": "Schindler's List", "rating": 9.0, "year": 1993, "genres": {"Docudrama", "Epic", "Historical Epic", "Period Drama", "Prison Drama", "Tragedy", "Biography", "Drama", "History"}},
  {"title": "The Shawshank Redemption", "rating": 9.3, "year": 1994, "genres": {"Epic", "Period Drama", "Prison Drama", "Drama"}},
  {"title": "Fight Club", "rating": 8.8, "year": 1999, "genres": {"Psychological Drama", "Workplace Drama", "Drama"}},
  {"title": "Pulp Fiction", "rating": 8.9, "year": 1994, "genres": {"Dark Comedy", "Drug Crime", "Gangster", "Crime", "Drama"}},
  {"title": "Scarface", "rating": 8.3, "year": 1983, "genres": {"Drug Crime", "Epic", "Gangster", "Tragedy", "Crime", "Drama"}},
  {"title": "The Green Mile", "rating": 8.6, "year": 1999, "genres": {"Period Drama", "Prison Drama", "Supernatural Fantasy", "Tragedy", "Crime", "Drama", "Fantasy", "Mystery"}},
  {"title": "Spirited Away", "rating": 8.6, "year": 2001, "genres": {"Anime", "Coming-of-Age", "Fairy Tale", "Hand-Drawn Animation", "Quest", "Supernatural Fantasy", "Adventure", "Animation", "Family", "Fantasy"}},
  {"title": "Pan's Labyrinth", "rating": 8.2, "year": 2006, "genres": {"Coming-of-Age", "Dark Fantasy", "Fairy Tale", "Period Drama", "Supernatural Fantasy", "Teen Fantasy", "Tragedy", "Drama", "Fantasy", "War"}},
  {"title": "How to Train Your Dragon", "rating": 8.1, "year": 2010, "genres": {"Computer Animation", "Sword & Sorcery", "Teen Fantasy", "Action", "Adventure", "Animation", "Family", "Fantasy"}},
  {"title": "Saving Private Ryan", "rating": 8.6, "year": 1998, "genres": {"Epic", "Period Drama", "War Epic", "Drama", "War"}},
  {"title": "Come and See", "rating": 8.3, "year": 1985, "genres": {"Epic", "Period Drama", "Tragedy", "War Epic", "Drama", "Thriller", "War"}},
  {"title": "Apocalypse Now", "rating": 8.4, "year": 1979, "genres": {"Adventure Epic", "Epic", "Psychological Drama", "Quest", "War Epic", "Drama", "Mystery", "War"}},
  {"title": "1917", "rating": 8.2, "year": 2019, "genres": {"Epic", "Period Drama", "War Epic", "Action", "Drama", "War"}},
  {"title": "Das Boot", "rating": 8.4, "year": 1981, "genres": {"Epic", "War Epic", "Drama", "War"}},
  {"title": "Im Westen nichts Neues", "rating": 7.8, "year": 2022, "genres": {"Epic", "Period Drama", "Tragedy", "War Epic", "Drama", "History", "War"}},
  {"title": "The Pianist", "rating": 8.5, "year": 2002, "genres": {"Docudrama", "Epic", "Period Drama", "Tragedy", "War Epic", "Biography", "Drama", "Music", "War"}},
  {"title": "Bo Burnham: Inside", "rating": 8.6, "year": 2021, "genres": {"Dark Comedy", "Psychological Drama", "Satire", "Stand-Up", "Comedy", "Documentary", "Drama", "Music"}},
  {"title": "Modern Times", "rating": 8.5, "year": 1936, "genres": {"Romantic Comedy", "Satire", "Slapstick", "Comedy", "Drama", "Romance"}},
  {"title": "The Great Dictator", "rating": 8.4, "year": 1940, "genres": {"Parody", "Satire", "Slapstick", "Comedy", "Drama", "War"}},
  {"title": "Parasite", "rating": 8.5, "year": 2019, "genres": {"Dark Comedy", "Korean Drama", "Psychological Thriller", "Tragedy", "Drama", "Thriller"}},
  {"title": "Mad Max: Fury Road", "rating": 8.1, "year": 2015, "genres": {"Action Epic", "Adventure Epic", "Car Action", "Desert Adventure", "Dystopian Sci-Fi", "Epic", "Quest", "Road Trip", "Action", "Adventure"}},
  {"title": "Dune: Part One", "rating": 8.0, "year": 2021, "genres": {"Desert Adventure", "Sci-Fi Epic", "Space Sci-Fi", "Action", "Adventure", "Drama", "Sci-Fi"}},
  {"title": "Dune: Part Two", "rating": 8.5, "year": 2024, "genres": {"Action Epic", "Desert Adventure", "Epic", "Sci-Fi Epic", "Space Sci-Fi", "Action", "Adventure", "Drama", "Sci-Fi"}},
  {"title": "Ghostbusters", "rating": 7.8, "year": 1984, "genres": {"High-Concept Comedy", "Quirky Comedy", "Supernatural Fantasy", "Action", "Comedy", "Fantasy", "Sci-Fi"}},
  {"title": "Home Alone", "rating": 7.7, "year": 1990, "genres": {"High-Concept Comedy", "Holiday Comedy", "Holiday Family", "Slapstick", "Comedy", "Family", "Holiday"}},
  {"title": "Who Framed Roger Rabbit", "rating": 7.7, "year": 1988, "genres": {"Adult Animation", "Buddy Comedy", "Hand-Drawn Animation", "High-Concept Comedy", "Parody", "Slapstick", "Adventure", "Animation", "Comedy", "Crime"}},
  {"title": "Wreck-It Ralph", "rating": 7.7, "year": 2012, "genres": {"Buddy Comedy", "Computer Animation", "High-Concept Comedy", "Motorsport", "Quest", "Urban Adventure", "Adventure", "Animation", "Comedy", "Family"}},
  {"title": "Being John Malkovich", "rating": 7.7, "year": 1999, "genres": {"Body Swap Comedy", "High-Concept Comedy", "Psychological Drama", "Satire", "Showbiz Drama", "Supernatural Fantasy", "Comedy", "Drama", "Fantasy"}},
  {"title": "Scott Pilgrim vs. the World", "rating": 7.5, "year": 2010, "genres": {"High-Concept Comedy", "Romantic Comedy", "Teen Comedy", "Teen Fantasy", "Teen Romance", "Action", "Comedy", "Fantasy", "Romance"}},
  {"title": "Men in Black", "rating": 7.3, "year": 1997, "genres": {"Alien Invasion", "Buddy Comedy", "Buddy Cop", "High-Concept Comedy", "Urban Adventure", "Action", "Adventure", "Comedy", "Sci-Fi"}},
  {"title": "The Mask", "rating": 7.0, "year": 1994, "genres": {"High-Concept Comedy", "Slapstick", "Superhero", "Comedy", "Crime", "Fantasy"}},
  {"title": "Idiocracy", "rating": 6.5, "year": 2006, "genres": {"Dark Comedy", "Dystopian Sci-Fi", "High-Concept Comedy", "Satire", "Adventure", "Comedy", "Sci-Fi", "Thriller"}},
  {"title": "Galaxy Quest", "rating": 7.4, "year": 1999, "genres": {"High-Concept Comedy", "Parody", "Space Sci-Fi", "Adventure", "Comedy", "Sci-Fi"}},
  {"title": "The Shining", "rating": 8.4, "year": 1980, "genres": {"Dark Comedy", "Psychological Drama", "Psychological Horror", "Supernatural Horror", "Drama", "Horror"}},
  {"title": "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb", "rating": 8.3, "year": 1964, "genres": {"Dark Comedy", "Farce", "Political Drama", "Satire", "Tragedy", "Comedy", "War"}},
  {"title": "The Wolf of Wall Street", "rating": 8.2, "year": 2013, "genres": {"Dark Comedy", "Docudrama", "Epic", "Raunchy Comedy", "Satire", "True Crime", "Biography", "Comedy", "Crime", "Drama"}},
  {"title": "A Clockwork Orange", "rating": 8.2, "year": 1971, "genres": {"Dark Comedy", "Dystopian Sci-Fi", "Crime", "Sci-Fi"}},
  {"title": "Full Metla Jacket", "rating": 8.2, "year": 1987, "genres": {"Dark Comedy", "Period Drama", "Drama", "War"}},
  {"title": "Fargo", "rating": 8.1, "year": 1996, "genres": {"Cop Drama", "Dark Comedy", "Police Procedural", "Tragedy", "Crime", "Drama", "Thriller"}},
  {"title": "Life of Brian", "rating": 8.0, "year": 1979, "genres": {"Dark Comedy", "Parody", "Satire", "Comedy"}},
  {"title": "Everything Everywhere All at Once", "rating": 7.8, "year": 2022, "genres": {"Adventure Epic", "Dark Comedy", "Martial Arts", "Sci-Fi Epic", "Action", "Adventure", "Comedy", "Drama", "Fantasy", "Sci-Fi"}},
  {"title": "American Psycho", "rating": 7.6, "year": 2000, "genres": {"Dark Comedy", "Psychological Drama", "Psychological Horror", "Serial Killer", "Slasher Horror", "Workplace Drama", "Crime", "Drama", "Horror"}},
  {"title": "Eraserhead", "rating": 7.3, "year": 1977, "genres": {"Body Horror", "Dark Comedy", "Monster Horror", "Fantasy", "Horror"}},
  {"title": "The Truman Show", "rating": 8.2, "year": 1998, "genres": {"Dark Comedy", "High-Concept Comedy", "Psychological Drama", "Satire", "Showbiz Drama", "Comedy", "Drama"}},
  {"title": "Barbie", "rating": 6.8, "year": 2023, "genres": {"High-Concept Comedy", "Quirky Comedy", "Satire", "Adventure", "Comedy", "Fantasy"}},
  {"title": "The Iron Giant", "rating": 8.1, "year": 1999, "genres": {"Alien Invasion", "Artificial Intelligence", "Hand-Drawn Animation", "High-Concept Comedy", "Kaiju", "Space Sci-Fi", "Action", "Adventure", "Animation", "Comedy"}},
  {"title": "Groundhog Day", "rating": 8.0, "year": 1993, "genres": {"Feel-Good Romance", "High-Concept Comedy", "Holiday Comedy", "Holiday Romance", "Romantic Comedy", "Comedy", "Drama", "Fantasy", "Romance"}},
  {"title": "Spider-Man: Across the Spider-Verse", "rating": 8.5, "year": 2023, "genres": {"Computer Animation", "Superhero", "Supernatural Fantasy", "Teen Adventure", "Urban Adventure", "Action", "Adventure", "Animation", "Family", "Fantasy"}},
  {"title": "Avengers: Endgame", "rating": 8.4, "year": 2019, "genres": {"Space Sci-Fi", "Superhero", "Time Travel", "Tragedy", "Action", "Adventure", "Drama", "Sci-Fi"}},
  {"title": "The Usual Suspects", "rating": 8.5, "year": 1995, "genres": {"Caper", "Gangster", "Heist", "Psychological Drama", "Psychological Thriller", "Suspense Mystery", "Whodunnit", "Crime", "Drama", "Mystery"}},
  {"title": "Ocean's Eleven", "rating": 7.7, "year": 2001, "genres": {"Caper", "Heist", "Crime", "Thriller"}},
  {"title": "Knives Out", "rating": 7.9, "year": 2019, "genres": {"Cozy Mystery", "Satire", "Whodunnit", "Comedy", "Crime", "Drama", "Mystery", "Thriller"}},
  {"title": "The Girl with the Dragon Tattoo", "rating": 7.8, "year": 2011, "genres": {"Psychological Drama", "Psychological Thriller", "Serial Killer", "Whodunnit", "Crime", "Drama", "Mystery", "Thriller"}},
  {"title": "The Hateful Eight", "rating": 7.8, "year": 2015, "genres": {"Period Drama", "Suspense Mystery", "Whodunnit", "Crime", "Drama", "Mystery", "Thriller", "Western"}},
  {"title": "The Name of the Rose", "rating": 7.7, "year": 1986, "genres": {"Period Drama", "Whodunnit", "Drama", "Mystery", "Thriller"}},
  {"title": "Lucky Number Slevin", "rating": 7.7, "year": 2006, "genres": {"Crime", "Drama", "Thriller"}},
  {"title": "City of God", "rating": 8.6, "year": 2002, "genres": {"Caper", "Coming-of-Age", "Gangster", "Crime", "Drama"}},
  {"title": "The Grand Budapest Hotel", "rating": 8.1, "year": 2014, "genres": {"Caper", "Quirky Comedy", "Adventure", "Comedy", "Crime"}},
  {"title": "Baby Driver", "rating": 7.5, "year": 2017, "genres": {"Caper", "Car Action", "Action", "Crime", "Drama", "Music"}},
  {"title": "Companion", "rating": 7.3, "year": 2025, "genres": {"Dark Comedy", "Psychological Thriller", "Sci-Fi", "Thriller", "Artificial Intelligence"}},
  {"title": "One Flew Over the Cuckoo's Nest", "rating": 8.7, "year": 1975, "genres": {"Medical Drama", "Psychological Drama", "Drama"}},
  {"title": "12 Angry Men", "rating": 9.0, "year": 1957, "genres": {"Legal Drama", "Psychological Drama", "Crime", "Drama"}}
]

# genre_set = set()
# genre_set.update(*[movie["genres"] for movie in movie_list])
# [print(x) for x in sorted(genre_set)]

my_movie_list = movie_list.copy()

def list_all(dict_list: list[dict], key: str, is_set: bool = False):
    list_all = [element[key] for element in dict_list]
    if is_set:
        my_set = set()
        my_set.update(*list_all)
    else:
        my_set = set(list_all)
    return sorted(my_set)

def count_all(dict_list, value_list, key, is_set = False):
    dict_list = []
    if is_set:
        count_list = 
    else:
        count_list = [len([1 for d in dict_list if value == d[key]]) for value in value_list]
    return count_list
sum()
years = list_all(movie_list, "year")
ratings = list_all(movie_list, "rating")
genres = list_all(movie_list, "genres", True)

print("Jahre:   ", years[0], "-", years[-1])
print("Bewertung:", ratings[0], "-", ratings[-1])
print("Genres:   ", len(genres))

class test:
    def __str__(self):
        print(f"{self.name}")
