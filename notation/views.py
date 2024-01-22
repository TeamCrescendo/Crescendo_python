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
from notation.transfet_utils import down_mp3,mp3_to_midi

@csrf_exempt
def get_youtube_info(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =Youtube_Info_Serializer(data=data)

        if serializer.is_valid():
            instance=serializer.save()
            print(data)
            json_data=JsonResponse(serializer.data, status=201)
            #mp3파일 다운받고 midi파일로 변환
            mp3_path=down_mp3.download_audio(instance.url)
            musicxml_path=mp3_to_midi.down_musicxml(mp3_path)
            #midi파일을 musicxml로 변환하기

            return ''
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)


# views.py in Django
from django.http import JsonResponse
import requests
import json
#스프링으로 전달하는 함수
def export_to_spring(request):
    # 가상의 데이터 생성 (실제 데이터 사용)
    muscixml_path='D:\\Crescendo_python\\download\\audio.musicxml'
    data_to_export = {'musicxmlfile': muscixml_path}

    # JSON 파일 생성
    json_data = json.dumps(data_to_export)

    # 스프링 서버 URL
    spring_url = 'http://spring-server-url/api/import-data'

    # HTTP POST 요청을 통해 JSON 파일 전송
    response = requests.post(spring_url, json=json_data, headers={'Content-Type': 'application/json'})

    # 스프링에서의 응답 확인
    spring_response = response.json()

    # 장고에서의 응답
    return JsonResponse({'django_response': 'Export successful', 'spring_response': spring_response})

