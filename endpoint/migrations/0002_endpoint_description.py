# Generated by Django 2.1 on 2018-08-27 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='descrpition'),
        ),
    ]
