# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import SensorDetailSerializer, MeasurementSerializer
from .models import Sensor




class SensorsChangesView(APIView):

    def get(self,request, pk=None):
        if pk is None:
            all_sensors = Sensor.objects.all()
            serialize = SensorDetailSerializer(all_sensors, many=True)
            return Response(serialize.data)
        else:
            sensor_instance = get_object_or_404(Sensor.objects.all(), id=pk)
            serializer = SensorDetailSerializer(sensor_instance)
            return Response(serializer.data)


    def post(self, request):
        article = request.data
        # Create an article from the above data
        serializer = SensorDetailSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            saved_sensor = serializer.save()
        return Response({"success": "Sensor '{}' created successfully".format(saved_sensor.name)})

    def put(self, request, pk):
        sensor_instance = get_object_or_404(Sensor.objects.all(), pk=pk)
        data = request.data
        serializer = SensorDetailSerializer(instance=sensor_instance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            sensor_saved = serializer.save()
        return Response({
            "success": "Sensor '{}' updated successfully".format(sensor_saved.name)
        })


class AddMeasurementView(APIView):

    def post(self, request):
        data = request.data
        # Create an article from the above data
        serializer = MeasurementSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved_measurements = serializer.save()
        return Response({"success": "Measurements '{}' created successfully"})


        
