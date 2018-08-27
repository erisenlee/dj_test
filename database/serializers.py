from rest_framework import serializers
from .models import DataBase


class DbSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBase
        fields = ('host', 'port', 'username', 'password', 'db', 'created', 'title')
        