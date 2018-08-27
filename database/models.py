from django.db import models

# Create your models here.

class DataBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    host = models.GenericIPAddressField('host', default='')
    port = models.IntegerField('port', default=3306)
    username = models.CharField('username', max_length=64)
    password = models.CharField('password', max_length=64)
    db = models.CharField('db', max_length=64)
    title= models.CharField('title', max_length=64,default='db config')


    def __str__(self):
        return '{}:{}/{}'.format(self.host, self.port, self.db)
    
    class Meta:
        ordering=('created',)
           