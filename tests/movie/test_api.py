import pytest
from factory import Faker
from rest_framework import status

from django.urls import reverse
from tests.movie.factories import PeopleFactory, MovieFactory


@pytest.mark.django_db
def test_movies_listing(client):
    people = PeopleFactory.create(name=Faker("name"), identifier=Faker("name"))
    movie = MovieFactory.create(title=Faker("name"), identifier=Faker("name"))
    movie.people.add(people)
    response = client.get(reverse("movies:movie-list"),)

    assert response.status_code == status.HTTP_200_OK

    assert response.json()["count"] == 1, response
