from django.db import models
from django.utils import timezone

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Measurement(models.Model):
    created_at = models.DateField(default=timezone.now)
    temperature = models.IntegerField()
    id_measurement = models.ForeignKey(Sensor, on_delete=models.CASCADE)


