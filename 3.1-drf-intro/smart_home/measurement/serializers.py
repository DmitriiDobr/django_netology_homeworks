from rest_framework import serializers
from .models import Measurement, Sensor


# TODO: опишите необходимые сериализаторы
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.description = validated_data.get('name', instance.name)
        instance.body = validated_data.get('description', instance.description)
        instance.save()
        return instance
