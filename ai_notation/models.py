
# models.py
from django.db import models

class client_ai_info(models.Model):
    # 필요한 api 값
    prompt=models.CharField(max_length=100)
    # input_audio=models.FileField()
    duration=models.IntegerField()
# serializers.py
from rest_framework import serializers

# class server_ai_info(client_ai_info):
#     top_k= 250
#     top_p= 0
#     temperature= 1
#     continuation= False
#     model_version= "stereo-large"
#     output_format= "mp3"
#     continuation_start= 0
#     multi_band_diffusion= False
#     normalization_strategy= "peak"
#     classifier_free_guidance= 3




class Ai_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = client_ai_info
        fields = '__all__'

