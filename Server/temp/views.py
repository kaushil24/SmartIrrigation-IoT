from django.shortcuts import render
from rest_framework import viewsets
from .models import Temp
from .serializers import TempSerializer

class TempView(viewsets.ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = TempSerializer