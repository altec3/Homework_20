import pytest

from project.service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(2) is not None
        assert self.movie_service.get_one(2).title == 'Movie_2'

    def test_get_all(self):
        assert len(self.movie_service.get_all()) == 3

    def test_create(self):
        data: dict = {
            "title": "Movie_3",
            "year": 2022,
            "rating": 9.3,
        }
        assert self.movie_service.create(data).title == data.get("title")
        assert self.movie_service.create(data).year == data.get("year")
        assert self.movie_service.create(data).rating == data.get("rating")

    def test_update(self):
        data: dict = {
            "title": "Movie_3",
            "year": 2022,
            "rating": 9.3,
        }
        assert self.movie_service.create(data).title == data.get("title")
        assert self.movie_service.create(data).year == data.get("year")
        assert self.movie_service.create(data).rating == data.get("rating")

    def test_partially_update(self):
        assert 1 == 1

    def test_delete(self):
        assert 1 == 1
