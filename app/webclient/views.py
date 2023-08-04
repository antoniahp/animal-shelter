from django.contrib.sites import requests
from django.db.models import Q
from django.shortcuts import render

from core.models import AnimalModel


def home(request):
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
    return render(request, "home.html", context)