# models.py
from django.db import models

class Youtube_Info(models.Model):
    url = models.CharField(max_length=100)

# serializers.py
from rest_framework import serializers

class Youtube_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube_Info
        fields = '__all__'
