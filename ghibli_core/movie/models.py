from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    """
        Movie
    """

    identifier = models.CharField(
        max_length=100,
        help_text="a Movie identifier",
        verbose_name="a Movie identifier",
        unique=True,
    )

    title = models.CharField(_("title"), max_length=250, unique=True)

    description = models.TextField(_("Description"), null=True, blank=True)

    director = models.CharField(_("director"), max_length=100)
    producer = models.CharField(_("producer"), max_length=100)

    people = models.ManyToManyField("People", verbose_name=_("People"), blank=True)

    release_date = models.PositiveIntegerField(default=0)
    rt_score = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self):
        return "{}".format(self.title)


class People(models.Model):
    """
        People
    """

    identifier = models.CharField(
        max_length=100,
        help_text="People identifier",
        verbose_name="People identifier",
        unique=True,
    )

    name = models.CharField(_("name"), max_length=100, unique=True)

    gender = models.CharField(_("gender"), max_length=100, null=True, blank=True)

    age = models.CharField(_("gender"), max_length=100, null=True, blank=True)

    eye_color = models.CharField(_("Eye color"), max_length=100, null=True, blank=True)

    hair_color = models.CharField(
        _("Hair color"), max_length=100, null=True, blank=True
    )

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "people"
        verbose_name_plural = "peoples"

    def __str__(self):
        return "{}".format(self.name)
