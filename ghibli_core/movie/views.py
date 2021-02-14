from django.views import generic

from ghibli_core.movie.models import Movie


class MovieListView(generic.ListView):
    model = Movie
    context_object_name = "movie_list"
    queryset = Movie.objects.all()
    template_name = "movie/movie_list.html"
