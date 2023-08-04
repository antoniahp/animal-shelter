from django.urls import path
from webclient.views import home


urlpatterns = [
    path('', home, name='home'),

]