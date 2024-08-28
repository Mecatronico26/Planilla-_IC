from django.shortcuts import render
from .models import Instrument

def instrument_list(request):
    instruments = Instrument.objects.all()  # Obtiene todos los instrumentos
    return render(request, 'instruments/test_copy.html', {'instruments': instruments})