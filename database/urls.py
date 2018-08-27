from django.urls import path, include
from rest_framework import routers
from .views import DbViewSet

router = routers.DefaultRouter()
router.register('db', DbViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]