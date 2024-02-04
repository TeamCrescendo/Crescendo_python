
# models.py
from django.db import models
from django.conf import settings
from base import AI_AUDIO_DOWN_PATH

class client_ai_info(models.Model):
    # 필요한 api 값
    account=models.CharField(max_length=100)
    prompt=models.CharField(max_length=100)
    duration=models.IntegerField()
    base_mp3=models.FileField(upload_to=AI_AUDIO_DOWN_PATH,null=True) # mp3 파일을 받는 필드 -> null 허용


from rest_framework import serializers
class Ai_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = client_ai_info
        fields = '__all__'

