from typing import Optional, List

from django.db.models import Q

from core.models import AnimalModel, AnimalGenderChoices
from ninja import Router, Schema, Query, FilterSchema


core_router = Router()

class AnimalsFilterSchema(FilterSchema):
    gender: Optional[str]
    vaccinated: Optional[bool]
    born_year: Optional[int]

    def custom_expression(self) -> Q:
        filter_criteria = Q()

        if self.vaccinated is not None:
            filter_criteria = filter_criteria & Q(vaccinated=self.vaccinated)

        if self.gender is not None:
            filter_criteria = filter_criteria & Q(gender=self.gender)

        if self.born_year is not None:
            filter_criteria = filter_criteria & Q(age__year=self.born_year)

        return filter_criteria




@core_router.get("/animals")
def get_animals(request, filters: AnimalsFilterSchema = Query(...)):

    filtered_animals = filters.filter(
        AnimalModel.objects.all()  # Queryset que contiene todos los animales
    )
    animals = []
    for animal in filtered_animals:
        animals.append({
            "name": animal.name,
            "gender": animal.gender,
            "vaccinated": animal.vaccinated,
            "breed": animal.breed,
            "age": animal.age,
            "description": animal.description,
            "picture": animal.picture.url,

        })

    return{"animals": animals}