from django.urls import path
from .views import instrument_list

urlpatterns = [
    path('', instrument_list, name='instrument_list'),  # Aquí debe estar vacío para que se mapee a /
]