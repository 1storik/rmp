import os
import random
import threading
import time

from django.http import JsonResponse
from django.shortcuts import render
from .models import HeatingSettings, TemperatureArchive
from .config import *
light_state = {
        'room1': 0,
        'room2': 'Off',
        'room3': 'Off',
        'room4': 'Off',
    }

temp_temperature = 0


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
    is_heating = request.COOKIES.get('is_heating')
    context = {
        'light_state': light_state,
        'temperature': temperature,
        'is_heating': is_heating,
        'LOWTHRESHOLD': LOWTHRESHOLD,
        'HIGHTHRESHOLD': HIGHTHRESHOLD,
    }
    return render(request, 'house/index.html', context=context)


def get_temperature(request):
    global temp_temperature
    temperature = random.randint(9, 31)
    temp_temperature = temperature
    heating_settings = HeatingSettings.objects.get(id=1)

    if temperature >= HIGHTHRESHOLD:
        heating_settings.is_heating = False
    elif temperature < LOWTHRESHOLD:
        heating_settings.is_heating = True
    heating_settings.save()
    response_data = {
        'temperature': temperature,
        'is_heating': heating_settings.is_heating
    }
    response = JsonResponse(response_data)
    response.set_cookie('temperature', temperature)
    response.set_cookie('is_heating', heating_settings.is_heating)
    return response


def change_threshold(request):
    if request.method == "POST":
        low_threshold = request.POST.get('LOW')
        high_threshold = request.POST.get('HIGH')
        config_file_path = "D:/pythonProject/rmp/house/config.py"
        print(high_threshold)
        with open(config_file_path, 'r') as config_file:
            config_data = config_file.read()
            config_data = config_data.replace(f"LOWTHRESHOLD = {LOWTHRESHOLD}", f"LOWTHRESHOLD = {low_threshold}")
            config_data = config_data.replace(f"HIGHTHRESHOLD = {HIGHTHRESHOLD}", f"HIGHTHRESHOLD = {high_threshold}")
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_data)
        temperature = request.COOKIES.get('temperature')
        is_heating = request.COOKIES.get('is_heating')
        context = {
            'light_state': light_state,
            'temperature': temperature,
            'is_heating': is_heating,
            'LOWTHRESHOLD': LOWTHRESHOLD,
            'HIGHTHRESHOLD': HIGHTHRESHOLD,
        }
        return render(request, 'house/index.html', context=context)

def timel(s):
    return str(int(s.split(":")[0])) + "." + s.split(":")[1]

def average_temp_page(request):
    average_temperatures = TemperatureArchive.objects.all()
    times = [float(timel(str(temperature.timestamp.time()))) for temperature in average_temperatures]
    temperatures = [float(temperature.temperature) for temperature in average_temperatures]
    print(times)
    context = {
        'times': times,
        'temperatures': temperatures
    }
    return render(request, 'house/about.html', context)

def writhe_for_time(interval):
    while True:
        seconds = time.time()
        temperature_archive = TemperatureArchive(timestamp=time.ctime(seconds), temperature=temp_temperature)
        temperature_archive.save()
        print("The time is %s" % time.ctime(seconds))
        time.sleep(interval)


t1 = threading.Thread(target=writhe_for_time, args=(30,), daemon=True)
t1.start()

