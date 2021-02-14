import pytest
from tests.movie.factories import MovieFactory, PeopleFactory
from factory import Faker


@pytest.mark.django_db
def test_people():
    people = PeopleFactory.create(name=Faker("name"), identifier=Faker("name"))
    assert people.id
    assert people.identifier


@pytest.mark.django_db
def test_movie():
    people = PeopleFactory.create(name=Faker("name"), identifier=Faker("name"))
    movie = MovieFactory.create(title=Faker("name"), identifier=Faker("name"))
    movie.people.add(people)
    assert movie.id
    assert movie.identifier
