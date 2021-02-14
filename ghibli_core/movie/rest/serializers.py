from rest_framework import serializers

from ghibli_core.movie.models import Movie, People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ("id", "name", "gender", "age")


class MovieSerializer(serializers.ModelSerializer):
    people = serializers.SerializerMethodField()

    def get_people(self, obj):
        people_query = obj.people.all()
        return PeopleSerializer(people_query, many=True).data

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "director",
            "producer",
            "release_date",
            "rt_score",
            "people",
        )
