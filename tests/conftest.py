import pytest
from unittest.mock import MagicMock

from project.dao.director import DirectorDAO
from project.dao.genre import GenreDAO
from project.dao.model.director import Director
from project.dao.model.genre import Genre
from project.dao.model.movie import Movie
from project.dao.movie import MovieDAO


@pytest.fixture()
def director_objects() -> dict:
    object_1 = Director(id=1, name='Director_1')
    object_2 = Director(id=2, name='Director_2')
    object_3 = Director(id=3, name='Director_3')
    return {1: object_1, 2: object_2, 3: object_3}


@pytest.fixture()
def genre_objects() -> dict:
    object_1 = Genre(id=1, name='Genre_1')
    object_2 = Genre(id=2, name='Genre_2')
    object_3 = Genre(id=3, name='Genre_3')
    return {1: object_1, 2: object_2, 3: object_3}


@pytest.fixture()
def movie_objects() -> dict:
    m1 = Movie(id=1, title='Movie_1', description='Description_1', trailer='Trailer_1', year=2022, rating=9.1,
               genre_id=1, director_id=1)
    m2 = Movie(id=2, title='Movie_2', description='Description_2', trailer='Trailer_2', year=2022, rating=9.2,
               genre_id=2, director_id=2)
    m3 = Movie(id=3, title='Movie_3', description='Description_3', trailer='Trailer_3', year=2022, rating=9.3,
               genre_id=3, director_id=3)
    return {1: m1, 2: m2, 3: m3, }


@pytest.fixture()
def director_dao(director_objects: dict):
    director = DirectorDAO(None)
    director.get_one = MagicMock(side_effect=director_objects.get)
    director.get_all = MagicMock(return_value=director_objects.values())
    director.create = MagicMock(return_value=director_objects[3])
    director.delete = MagicMock()
    director.update = MagicMock(return_value=director_objects[3])
    return director


@pytest.fixture()
def genre_dao(genre_objects: dict):
    genre = GenreDAO(None)
    genre.get_one = MagicMock(side_effect=genre_objects.get)
    genre.get_all = MagicMock(return_value=genre_objects.values())
    genre.create = MagicMock(return_value=genre_objects[3])
    genre.delete = MagicMock()
    genre.update = MagicMock(return_value=genre_objects[3])
    return genre


@pytest.fixture()
def movie_dao(movie_objects: dict):
    movie = MovieDAO(None)
    movie.get_one = MagicMock(side_effect=movie_objects.get)
    movie.get_all = MagicMock(return_value=movie_objects.values())
    movie.create = MagicMock(return_value=movie_objects[3])
    movie.delete = MagicMock()
    movie.update = MagicMock(return_value=movie_objects[3])
    return movie
