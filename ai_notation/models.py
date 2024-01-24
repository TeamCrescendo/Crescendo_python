
# models.py
from django.db import models

class ai_info(models.Model):
    # 필요한 api 값
    model_version=models.CharField(max_length=100)
    prompt=models.CharField(max_length=100)
    input_audio=models.FileField()

# serializers.py
from rest_framework import serializers

class Ai_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ai_info
        fields = '__all__'