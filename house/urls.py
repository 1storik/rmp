from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from house.views import *

urlpatterns = [
    path('', index, name="house"),
    path('get_temperature/', get_temperature, name='get_temperature'),
    path('change_threshold/', change_threshold, name='change_threshold'),
    path('about/', average_temp_page, name='about'),
]
