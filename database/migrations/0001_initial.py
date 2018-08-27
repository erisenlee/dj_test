# Generated by Django 2.1 on 2018-08-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('host', models.GenericIPAddressField(default='', verbose_name='host')),
                ('port', models.IntegerField(default=3306, verbose_name='port')),
                ('username', models.CharField(max_length=64, verbose_name='username')),
                ('password', models.CharField(max_length=64, verbose_name='password')),
                ('db', models.CharField(max_length=64, verbose_name='db')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
