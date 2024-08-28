from django.shortcuts import render
from .models import Instrument

def instrument_list(request):
    instruments = Instrument.objects.all()
    return render(request, 'instruments/test.html', {'instruments': instruments})