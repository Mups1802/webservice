from rest_framework import serializers
from .models import Temperature, Humidity


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['Temperature']

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = ['Humidity']
