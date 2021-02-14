import requests
from django.conf import settings

from ghibli_core.movie.models import Movie, People


class GhibliUtility:
    """
        Ghibli utility class user to retrieve data and store in database
    """

    def get_and_save_movies(self):
        response = requests.get(settings.GHIBLI_API_URL + "films")
        if response:
            for resp in response.json():
                if not Movie.objects.filter(identifier=resp["id"]).exists():
                    Movie.objects.create(
                        identifier=resp["id"],
                        title=resp["title"],
                        description=resp["description"],
                        director=resp["director"],
                        producer=resp["producer"],
                        release_date=resp["release_date"],
                        rt_score=resp["rt_score"],
                    )

    def get_and_save_people(self):
        response = requests.get(settings.GHIBLI_API_URL + "people")
        if response:
            for resp in response.json():
                if not People.objects.filter(identifier=resp["id"]).exists():
                    people_instance = People.objects.create(
                        identifier=resp["id"],
                        name=resp["name"],
                        gender=resp["gender"],
                        age=resp["age"],
                        eye_color=resp["eye_color"],
                        hair_color=resp["hair_color"],
                    )

                    for film in resp["films"]:
                        movie = Movie.objects.get(
                            identifier=film.rsplit("films/", 1).pop()
                        )
                        movie.people.add(people_instance)

                else:
                    for film in resp["films"]:
                        movie = Movie.objects.get(
                            identifier=film.rsplit("films/", 1).pop()
                        )
                        people_instance = People.objects.get(identifier=resp["id"])
                        if not Movie.objects.filter(
                            identifier=movie.identifier, people__id=people_instance.id
                        ).exists():
                            movie.people.add(people_instance)
