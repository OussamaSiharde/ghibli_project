from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from ghibli_core.movie.rest.views import MovieViewSet

router = DefaultRouter()

router.register(r"movies", MovieViewSet)

app_name = "movies"

urlpatterns = [
    path("", include(router.urls)),
]
