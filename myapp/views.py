from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Temperature, Humidity
from .serializer import TemperatureSerializer, HumiditySerializer

class TemperatureDetailView(generics.RetrieveAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer

class TemperatureListView(generics.ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer

class TemperatureCreateAPIView(generics.CreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer
    
class LatestTemperatureAPIView(APIView):
    def get(self, request):
        latest_temperature = Temperature.objects.latest('id')
        return Response({"temperature": latest_temperature.data})
class LatestHumidityTemperatureAPIView(APIView):
    def get(self, request):
        latest_humidity = Humidity.objects.latest('id')
        return Response({"humidity": latest_humidity.data})


def temperature_monitor(request):
    return render(request, 'temperature.html')
