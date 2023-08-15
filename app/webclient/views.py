import requests
from django.db.models import Q
from django.shortcuts import render

from core.models import AnimalModel
from django.shortcuts import redirect
from django.urls import reverse


"""def home(request):
    filter_criteria = Q()

    if request.method == 'POST':
        vaccinated = request.POST.get("vaccinated")
        gender = request.POST.get("gender")
        age = request.POST.get("age")

        if vaccinated == "true":
            filter_criteria = filter_criteria & Q(vaccinated=True)
        if vaccinated == "false":
            filter_criteria = filter_criteria & Q(vaccinated=False)

        if gender == "MALE":
            filter_criteria = filter_criteria & Q(gender="MALE")
        if gender == "FEMALE":
            filter_criteria = filter_criteria & Q(gender="FEMALE")

       # Hace lo mismo y es más simple.
       # if gender != "":
       #     filter_criteria = filter_criteria & Q(gender=gender)

        if age != "":
            filter_criteria = filter_criteria & Q(age__year=age)

    context = {
        "animals": AnimalModel.objects.filter(filter_criteria)

    }
    return render(request, "home.html", context) """

def home(request):
    query_params = {}
    if request.method == 'POST':
        vaccinated = request.POST.get("vaccinated")
        if vaccinated != "":
            query_params["vaccinated"] = vaccinated

        gender = request.POST.get("gender")
        if gender != "":
            query_params["gender"] = gender

        age = request.POST.get("age")
        if age != "":
            query_params["age"] = age

    response = requests.get(url="http://localhost:8000/api/core/animals", params=query_params)
    response.raise_for_status()


    animal_list_from_api = response.json()["animals"]
    context = {
        "animals": animal_list_from_api

    }
    return render(request, "home.html", context)