import json
import random

from django.http import JsonResponse
from django.shortcuts import render
light_state = {
        'room1': 0,
        'room2': 'Off',
        'room3': 'Off',
        'room4': 'Off',
    }


def index(request):

    if request.method == 'POST':
        if 'light_opacity' in request.POST:
            light_state['room1'] = int(request.POST['light_opacity'])

        if 'light_on_room2' in request.POST:
            light_state['room2'] = 'On'
        elif 'light_off_room2' in request.POST:
            light_state['room2'] = 'Off'

        if 'light_on_room3' in request.POST:
            light_state['room3'] = 'On'
        elif 'light_off_room3' in request.POST:
            light_state['room3'] = 'Off'

        if 'light_on_room4' in request.POST:
            light_state['room4'] = 'On'
        elif 'light_off_room4' in request.POST:
            light_state['room4'] = 'Off'
    temperature = request.COOKIES.get('temperature')
    context = {
        'light_state': light_state,
        'temperature': temperature,
    }
    return render(request, 'house/index.html', context=context)


def get_temperature(request):
    temperature = random.randint(20, 30)
    response = JsonResponse({'temperature': temperature})
    response.set_cookie('temperature', temperature)
    return response
