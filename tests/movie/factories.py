import factory
from ghibli_core.movie.models import Movie, People


class PeopleFactory(factory.DjangoModelFactory):
    class Meta:
        model = People


class MovieFactory(factory.DjangoModelFactory):
    class Meta:
        model = Movie
