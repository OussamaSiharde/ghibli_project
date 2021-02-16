# Generated by Django 3.0 on 2021-02-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="People",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "identifier",
                    models.CharField(
                        help_text="People identifier",
                        max_length=100,
                        unique=True,
                        verbose_name="People identifier",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="name"),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="gender"
                    ),
                ),
                (
                    "age",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="gender"
                    ),
                ),
                (
                    "eye_color",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Eye color"
                    ),
                ),
                (
                    "hair_color",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Hair color"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
            ],
            options={
                "verbose_name": "people",
                "verbose_name_plural": "peoples",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "identifier",
                    models.CharField(
                        help_text="a Movie identifier",
                        max_length=100,
                        unique=True,
                        verbose_name="a Movie identifier",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=250, unique=True, verbose_name="title"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                ("director", models.CharField(max_length=100, verbose_name="director")),
                ("producer", models.CharField(max_length=100, verbose_name="producer")),
                ("release_date", models.PositiveIntegerField(default=0)),
                ("rt_score", models.PositiveIntegerField(default=0)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "people",
                    models.ManyToManyField(
                        blank=True, to="movie.People", verbose_name="People"
                    ),
                ),
            ],
            options={
                "verbose_name": "movie",
                "verbose_name_plural": "movies",
                "ordering": ("title",),
            },
        ),
    ]