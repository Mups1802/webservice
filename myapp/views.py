from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Temperature
from .serializer import TemperatureSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json 

class TemperatureDetailView(generics.RetrieveAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureListView(generics.ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureCreateAPIView(generics.CreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    
class LatestTemperatureAPIView(APIView):
    def get(self, request):
        latest_temperature = Temperature.objects.latest('id')
        return Response({"temperature": latest_temperature.data})

def temperature_monitor(request):
    return render(request, 'temperature.html')
