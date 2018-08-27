from .models import BaseUrl, EndPoint
from rest_framework import serializers


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseUrl
        fields = ('host', 'created')

class EndPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EndPoint
        fields=('endpoint','hostname','description','created')