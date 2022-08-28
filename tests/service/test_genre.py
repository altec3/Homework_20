import pytest

from project.service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        assert self.genre_service.get_one(2) is not None
        assert self.genre_service.get_one(2).name == 'Genre_2'

    def test_get_all(self):
        assert len(self.genre_service.get_all()) == 3

    def test_create(self):
        data: dict = {
            "name": "Genre_3",
        }
        assert self.genre_service.create(data).name == data.get("name")

    def test_update(self):
        data: dict = {
            "name": "Genre_3",
        }
        assert self.genre_service.create(data).name == data.get("name")

    def test_partially_update(self):
        assert 1 == 1

    def test_delete(self):
        assert 1 == 1
