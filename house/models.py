from django.db import models


class HeatingSettings(models.Model):
    is_heating = models.BooleanField(null=True)


class TemperatureArchive(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
