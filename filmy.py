import random
from datetime import datetime

# Library was generated by ChatGPT
library = [
    {"type": "movie", "title": "The Matrix", "year": 1999, "genre": "Sci-Fi"},
    {"type": "movie", "title": "Inception", "year": 2010, "genre": "Action"},
    {"type": "movie", "title": "The Godfather", "year": 1972, "genre": "Crime"},
    {"type": "movie", "title": "The Dark Knight", "year": 2008, "genre": "Action"},
    {"type": "movie", "title": "Pulp Fiction", "year": 1994, "genre": "Drama"},
    {"type": "movie", "title": "Forrest Gump", "year": 1994, "genre": "Drama"},
    {"type": "movie", "title": "Fight Club", "year": 1999, "genre": "Drama"},
    {"type": "movie", "title": "Interstellar", "year": 2014, "genre": "Sci-Fi"},
    {"type": "movie", "title": "The Shawshank Redemption", "year": 1994, "genre": "Drama"},
    {"type": "movie", "title": "The Avengers", "year": 2012, "genre": "Action"},

    {"type": "series", "title": "Breaking Bad", "year": 2008, "genre": "Crime", "season": 5, "episode": 2},
    {"type": "series", "title": "Game of Thrones", "year": 2011, "genre": "Fantasy", "season": 8, "episode": 3},
    {"type": "series", "title": "Stranger Things", "year": 2016, "genre": "Sci-Fi", "season": 4, "episode": 3},
    {"type": "series", "title": "The Office", "year": 2005, "genre": "Comedy", "season": 9, "episode": 1},
    {"type": "series", "title": "Friends", "year": 1994, "genre": "Comedy", "season": 10, "episode": 6},
    {"type": "series", "title": "The Mandalorian", "year": 2019, "genre": "Sci-Fi", "season": 3, "episode": 4},
    {"type": "series", "title": "The Crown", "year": 2016, "genre": "Drama", "season": 5, "episode": 5},
    {"type": "series", "title": "The Witcher", "year": 2019, "genre": "Fantasy", "season": 3, "episode": 10},
    {"type": "series", "title": "The Boys", "year": 2019, "genre": "Action", "season": 4, "episode": 4},
    {"type": "series", "title": "The Walking Dead", "year": 2010, "genre": "Horror", "season": 11, "episode": 17},

    {"type": "movie", "title": "Parasite", "year": 2019, "genre": "Thriller"},
    {"type": "movie", "title": "Titanic", "year": 1997, "genre": "Romance"},
    {"type": "movie", "title": "Avatar", "year": 2009, "genre": "Sci-Fi"},
    {"type": "movie", "title": "Joker", "year": 2019, "genre": "Drama"},
    {"type": "movie", "title": "Schindler's List", "year": 1993, "genre": "History"},
    {"type": "movie", "title": "The Lion King", "year": 1994, "genre": "Animation"},
    {"type": "movie", "title": "The Lord of the Rings: The Return of the King", "year": 2003, "genre": "Fantasy"},
    {"type": "movie", "title": "Gladiator", "year": 2000, "genre": "Action"},
    {"type": "movie", "title": "The Silence of the Lambs", "year": 1991, "genre": "Thriller"},
    {"type": "movie", "title": "Saving Private Ryan", "year": 1998, "genre": "War"},

    {"type": "series", "title": "The Simpsons", "year": 1989, "genre": "Comedy", "season": 34, "episode": 15},
    {"type": "series", "title": "Rick and Morty", "year": 2013, "genre": "Sci-Fi", "season": 7, "episode": 7},
    {"type": "series", "title": "The Sopranos", "year": 1999, "genre": "Crime", "season": 6, "episode": 8},
    {"type": "series", "title": "House of Cards", "year": 2013, "genre": "Drama", "season": 6, "episode": 7},
    {"type": "series", "title": "Narcos", "year": 2015, "genre": "Crime", "season": 3, "episode": 3},
    {"type": "series", "title": "Black Mirror", "year": 2011, "genre": "Sci-Fi", "season": 6, "episode": 7},
    {"type": "series", "title": "Peaky Blinders", "year": 2013, "genre": "Crime", "season": 6, "episode": 3},
    {"type": "series", "title": "Westworld", "year": 2016, "genre": "Sci-Fi", "season": 4, "episode": 6},
    {"type": "series", "title": "Better Call Saul", "year": 2015, "genre": "Crime", "season": 6, "episode": 6},
    {"type": "series", "title": "Ozark", "year": 2017, "genre": "Crime", "season": 4, "episode": 4},

    {"type": "movie", "title": "The Prestige", "year": 2006, "genre": "Thriller"},
    {"type": "movie", "title": "Whiplash", "year": 2014, "genre": "Drama"},
    {"type": "movie", "title": "Django Unchained", "year": 2012, "genre": "Western"},
    {"type": "movie", "title": "The Social Network", "year": 2010, "genre": "Drama"},
    {"type": "movie", "title": "Mad Max: Fury Road", "year": 2015, "genre": "Action"},
    {"type": "movie", "title": "The Green Mile", "year": 1999, "genre": "Drama"},
    {"type": "movie", "title": "A Beautiful Mind", "year": 2001, "genre": "Biography"},
    {"type": "movie", "title": "The Wolf of Wall Street", "year": 2013, "genre": "Drama"},
    {"type": "movie", "title": "La La Land", "year": 2016, "genre": "Musical"}]
library_titles = []

class Movie:
    def __init__(self,title,year,genre):
          self.title = title
          self.genre = genre
          self.year = year
          self.views = 0 #views are assumed to be 0 by default

    def __str__(self):
        return f"{self.title} ({self.year})"
    
    def play(self):
         self.views += 1
    
class Series(Movie):
    def __init__(self,season,episode,*args,**kwargs):
          super().__init__(*args, **kwargs)
          self.season = season
          self.episode = episode

    def __str__(self):
         if len(str(self.season))==1:
              self.season="0"+str(self.season)
         if len(str(self.episode))==1:
              self.episode="0"+str(self.episode)
         return f"{self.title} S{self.season}E{self.episode}"

# Classifying the library items
for item in library:
    if item['type'] == 'movie':
        movie = Movie(title=item['title'], year=item['year'], genre=item['genre'])
        library_titles.append(movie)
    elif item['type'] == 'series':
        series = Series(title=item['title'], year=item['year'], genre=item['genre'], season=item['season'], episode=item['episode'])
        library_titles.append(series)

# Function which searches for an item in the library by item
def search(input_title):
    for item in library_titles:
         if item.title == input_title:
              return item

# Function which sorts movies from the library
def get_movies(library_titles):
    my_movies = []
    for item in library_titles:
        if not isinstance(item,Series):
            my_movies.append(item)
    return sorted(my_movies,key=lambda item: item.title)

# Function which sorts the series from the library
def get_series(library_titles):
     my_series = []
     for item in library_titles:
          if isinstance(item,Series):
               my_series.append(item)
     return sorted(my_series,key=lambda item: item.title)

# Generating random views numbers
def generate_views(item):
     item.views += random.randint(1, 100)

def views_for_today(library_titles):
    for i in range(10):
         generate_views(library_titles[random.randint(0,len(library_titles)-1)])

# Function returning top titles based on views
def top_titles(library_titles,number,content_type=None):
     if content_type == Series:
        library_titles_sorted=sorted(get_series(library_titles), key = lambda item: item.views, reverse=True)
     elif content_type == Movie:
        library_titles_sorted=sorted(get_movies(library_titles), key = lambda item: item.views, reverse=True)
     else:
        library_titles_sorted=sorted(library_titles, key = lambda item: item.views, reverse=True)
     for i in range(number):
          print(library_titles_sorted[i])

# Function completing the series for known series in the library
def complete_series(input_title,season_number,episodes_number):
    series_to_complete = search(input_title)
    for i in range(episodes_number):
        new_episode = Series(title=series_to_complete.title,year=series_to_complete.year, genre=series_to_complete.genre, season=season_number, episode=i+1)
        library_titles.append(new_episode)

print("Biblioteka filmów i seriali:")
for item in library_titles:
    print(item)

views_for_today(library_titles)
now = datetime.now()
today_date = now.date()
today_date = today_date.strftime("%d.%m.%Y")
print(f"Najpopularniejsze filmy i seriale dnia {today_date}:")
top_titles(library_titles,3)
