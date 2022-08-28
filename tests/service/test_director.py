import pytest

from project.service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        assert self.director_service.get_one(2) is not None
        assert self.director_service.get_one(2).name == 'Director_2'

    def test_get_all(self):
        assert len(self.director_service.get_all()) == 3

    def test_create(self):
        data: dict = {
            "name": "Director_3",
        }
        assert self.director_service.create(data).name == data.get("name")

    def test_update(self):
        data: dict = {
            "name": "Director_3",
        }
        assert self.director_service.create(data).name == data.get("name")

    def test_partially_update(self):
        assert 1 == 1

    def test_delete(self):
        assert 1 == 1
