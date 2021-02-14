from django.urls import include, path

urlpatterns = [
    path("", include("ghibli_core.movie.urls")),
]
