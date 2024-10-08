from django.db import models
from django.core.validators import MinLengthValidator
from Petstagram.pets.models import Pet
from Petstagram.photos.validators import FileSizeValidator


# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(
        upload_to='mediafiles',
        validators=[
        FileSizeValidator(5)
    ])
    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10)],
        null=True,
        blank=True
    )
    location = models.CharField(max_length=30, null=True, blank=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)