import random
import whole_library as wl
from movies import Movie
from series import Series
from datetime import date

library = [wl.friends, wl.killer, wl.intouchables, wl.matrix]
movies_library = []
series_library = []


def get_movies(lib):
    for i in lib:
        if isinstance(i, Movie) and not isinstance(i, Series):
            movies_library.append(i)
    movies_library.sort(key=lambda movie: movie.title)


def get_series(lib):
    for i in lib:
        if isinstance(i, Series):
            series_library.append(i)
    series_library.sort(key=lambda series: series.title)


def search(title):
    found = False
    for obj in library:
        if obj.title == title:
            found = True
    if found:
        print("Found")
    else:
        print('Not found')


def generate_views():
    random_pick = random.choice(library)
    random_views = random.randint(1, 101)
    random_pick.views += random_views


def run_views_generator():
    for i in range(10):
        generate_views()


def top_titles(number_of_titles):
    content = input("Series (s) or movies (m)?")
    if content == 'm':
        movies_library.sort(key=lambda movie: movie.views)
        for i in range(number_of_titles):
            print(movies_library[i])
    elif content == 's':
        series_library.sort(key=lambda movie: movie.views)
        for i in range(number_of_titles):
            print(series_library[i])
    else:
        print("Unknown command")


def season_adder(object_title, released, genre, season_nr, num_of_episodes):
    object_title.season_nr = season_nr
    for ep in range(1, num_of_episodes + 1):
        object_title.episode_nr.append(ep)
# Jak dla mnie treść zadania jest trochę bez sensu/ niezrozumiała stąd taka funkcja.


def welcome_display():
    get_movies(library)
    generate_views()
    print(movies_library)
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    print("Biblioteka filmów")
    print(f"Najpopularniejsze filmy i seriale dnia {d1}")

    movies_library.sort(key=lambda movie: movie.views)
    for i in range(3):
        print(movies_library[i])


welcome_display()
