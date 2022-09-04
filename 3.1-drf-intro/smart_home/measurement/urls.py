from django.urls import path
from django.contrib import admin
from .views import AddMeasurementView, SensorsChangesView

urlpatterns = [
               path("measurements/", AddMeasurementView.as_view()), 
               path("sensors/", SensorsChangesView.as_view()),
               path("sensors/<int:pk>/", SensorsChangesView.as_view()),
               
    # TODO: зарегистрируйте необходимые маршруты
]
