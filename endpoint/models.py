from django.db import models

# Create your models here.

class BaseUrl(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    host = models.CharField('host', max_length=300, default='')
    
    def __str__(self):
        return self.host


class EndPoint(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    endpoint = models.CharField('endpoint', blank=True, null=True, max_length=250, default='')
    hostname=models.ForeignKey('BaseUrl',on_delete=models.CASCADE)
    description=models.CharField('descrpition',max_length=300,blank=True, null=True)
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return '{}'.format(self.endpoint)