import pytest
import vcr

from ghibli_core.movie.models import Movie, People
from ghibli_core.movie.utils import GhibliUtility

scrape_vcr = vcr.VCR(
    serializer="yaml",
    path_transformer=vcr.VCR.ensure_suffix(".yaml"),
    cassette_library_dir="tests/movie/cassettes",
    record_mode="once",
    match_on=("method", "scheme", "port", "path", "query"),
)


@pytest.mark.django_db
@scrape_vcr.use_cassette(match_on=("method", "path"))
def test_ghibli_api_integration():
    GhibliUtility().get_and_save_movies()
    assert Movie.objects.all()

    GhibliUtility().get_and_save_people()
    assert People.objects.all()

    GhibliUtility().get_and_save_movies()
    assert Movie.objects.all()

    GhibliUtility().get_and_save_people()
    assert People.objects.all()
