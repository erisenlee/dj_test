# from django.shortcuts import render
from .models import EndPoint, BaseUrl
from rest_framework import viewsets
from .serializers import HostSerializer,EndPointSerializer

# Create your views here.


class HostViewSet(viewsets.ModelViewSet):
    
    queryset = BaseUrl.objects.all().order_by('created')
    serializer_class = HostSerializer

class EndPointtViewSet(viewsets.ModelViewSet):
    queryset = EndPoint.objects.all().order_by('created')
    serializer_class = EndPointSerializer


