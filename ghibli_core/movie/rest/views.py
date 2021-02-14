import logging

from rest_framework import viewsets, mixins

from ghibli_core.movie.models import Movie
from ghibli_core.movie.rest.paginations import StandardResultsSetPagination
from ghibli_core.movie.rest.serializers import MovieSerializer

logger = logging.getLogger(__name__)


class MovieViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    pagination_class = StandardResultsSetPagination
