from core.models import AnimalModel
from ninja import Router


core_router = Router()

@core_router.get("/animals")
def get_animals(request):
    animals = []
    for animal in AnimalModel.objects.filter():
        animals.append({
            "name": animal.name,
            "gender": animal.gender,
            "vaccinated": animal.vaccinated,
            "breed": animal.breed,
            "age": animal.age,
            "description": animal.description,
            "picture": animal.picture.url,

        })
        return{"animals":animals}