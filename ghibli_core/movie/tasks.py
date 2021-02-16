import logging
from celery.task import task
from celery import shared_task

from ghibli_core.movie.utils import GhibliUtility

logger = logging.getLogger("celery")


@shared_task
def sync_data():
    logger.info("sync_data running")
    get_and_save_movies.apply_async()
    get_and_save_people.apply_async()


@task(name="movie.get_and_save_movies", max_retries=3, bind=True)
def get_and_save_movies(self):
    try:
        ghibli_utility = GhibliUtility()
        ghibli_utility.get_and_save_movies()
    except Exception as exc:
        # retry when parsing fails
        logger.error("Failed to get movie data", extra={"exception": exc})
        raise self.retry(kwargs={}, exc=exc, countdown=10)


@task(name="movie.get_and_save_people", max_retries=3, bind=True)
def get_and_save_people(self):
    try:
        ghibli_utility = GhibliUtility()
        ghibli_utility.get_and_save_people()
    except Exception as exc:
        # retry when parsing fails
        logger.error("Failed to get people data", extra={"exception": exc})
        raise self.retry(kwargs={}, exc=exc, countdown=10)
