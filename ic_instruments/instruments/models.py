from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    calibration_date = models.DateField()
    last_maintenance = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name