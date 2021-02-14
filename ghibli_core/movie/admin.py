from django.contrib import admin
from ghibli_core.movie.models import People, Movie


class MovieAdmin(admin.ModelAdmin):
    """MovieAdmin
    """

    model = Movie
    list_display = ("title", "director", "producer", "release_date", "rt_score")
    filter_horizontal = ("people",)
    list_per_page = 15


class PeopleAdmin(admin.ModelAdmin):
    """PeopleAdmin
    """

    model = People
    list_display = ("name", "gender", "age")
    list_per_page = 15


admin.site.register(Movie, MovieAdmin)
admin.site.register(People, PeopleAdmin)
