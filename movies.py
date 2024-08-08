import datetime

import database


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ") or datetime.datetime.today().strftime("%d-%m-%Y")
    try:
        release_timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestamp()
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-YYYY format.")
        return
    database.add_movie(title, release_timestamp)


# movies.py


def print_movie_list(title, movies):
    
    print(f"-- {title} movies --")
    
    for movie in movies:
        name, genre, movie_date = movie
        
        if isinstance(movie_date, str):
            # We assume the date is in the format 'MMM dd YYYY'
            movie_date = datetime.datetime.strptime(movie_date, '%b %d %Y').timestamp()
        movie_date = datetime.datetime.fromtimestamp(movie_date)
        print(f"{name} ({genre}) - {movie_date.strftime('%b %d %Y')}")


def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username, movie_id)


def prompt_get_watched_movies():
    username = input("Username: ")
    return database.get_watched_movies(username)


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


def prompt_search_movies():
    search_term = input("Enter partial movie title: ")
    return database.search_movies(search_term)
