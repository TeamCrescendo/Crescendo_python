
# models.py
from django.db import models

class client_ai_info(models.Model):
    # 필요한 api 값
    account=models.CharField(max_length=100)
    prompt=models.CharField(max_length=100)
    duration=models.IntegerField()


from rest_framework import serializers
class Ai_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = client_ai_info
        fields = '__all__'

