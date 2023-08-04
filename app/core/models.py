from django.db import models
from datetime import date


class AnimalGenderChoices(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"

class AnimalVaccinatedChoices(models.TextChoices):
    NOT_VACCINATED = "NOT VACCINATED"
    VACCINATED = "VACCINATED"

class AnimalModel(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=AnimalGenderChoices.choices)
    vaccinated = models.BooleanField()
    breed = models.CharField(max_length=50)
    age = models.DateField()
    description = models.TextField()
    picture = models.ImageField()

    def __str__(self) -> str:
        return f"{self.name}"