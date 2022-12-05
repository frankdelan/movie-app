from .kinopoisk_api import KP, FILM
from .token import token
kinopoisk = KP(token=token)


def get_films_data(title: str) -> list:
    films: list = kinopoisk.search(title)
    return films


def get_film_by_id(movie_id: int) -> FILM:
    film: FILM = kinopoisk.get_film(movie_id)
    return film
