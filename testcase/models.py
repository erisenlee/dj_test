from django.db import models

# Create your models here.


class TestCase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    