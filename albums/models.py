from django.core.validators import MinValueValidator
from django.db import models

import albums.choices
import profiles.models


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(
        unique=True,
        max_length=30
    )
    artist = models.CharField(
        max_length=30
    )
    genre = models.CharField(
        max_length=30,
        choices=albums.choices.AlbumChoices,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField()
    price = models.FloatField(
        validators=[
            MinValueValidator(0.0)
        ],
    )
    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='albums',
    )