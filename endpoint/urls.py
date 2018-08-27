from django.conf.urls import url,include
from rest_framework import routers
from .views import HostViewSet, EndPointtViewSet
from .models import BaseUrl,EndPoint

router = routers.DefaultRouter()

router.register(r'host', HostViewSet)
router.register(r'endpoint', EndPointtViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    
]