from django.shortcuts import render
from rest_framework import generics,status
""" 여기가 service 부분 """
# Create your views here.
# url 요청이 들어오면 역직력화 해서 url얻기
#url 얻어서  down_mp3로 보내서 mp3획득
#mp3 파일로 스포티파이 api 이용한 midi 파일 얻는 함수에 넣고 midi파일 값 얻기

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from notation.models import Youtube_Info_Serializer
from notation.transfet_utils import down_mp3

@csrf_exempt
def get_youtube_info(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =Youtube_Info_Serializer(data=data)

        if serializer.is_valid():
            instance=serializer.save()
            print(data)
            json_data=JsonResponse(serializer.data, status=201)
            return down_mp3.download_audio(instance.url)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

