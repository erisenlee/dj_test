# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DbSerializer
from .models import DataBase
# Create your views here.

class DbViewSet(viewsets.ModelViewSet):
    queryset = DataBase.objects.all().order_by('created')
    serializer_class = DbSerializer
    
    

