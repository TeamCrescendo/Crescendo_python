from django.shortcuts import render
from rest_framework import generics,status
""" 여기가 service 부분 """
# Create your views here.
'''
ai음악생성 api 값 목록
model_version String : 기본값 stereo-melody-large
"input_audio" file
"top_k": 250,
"top_p": 0,
"prompt": "Edo25 major g melodies that sound triumphant and cinematic. Leading up to a crescendo that resolves in a 9th harmonic",
"duration": integer : 오디오 생성 시간,
"temperature": 1,
"continuation": boolean : true 원래 음악에 연결되는 음악생성, false : 인풋 오디오에기반한 새로운 음악
"output_format": "mp3",-> 고정사항
"continuation_start": 0, continuation가 참일 경우 몇초부터 연결되는 음악을 생성할 것인지
"multi_band_diffusion": False,-> 고정
"normalization_strategy": "peak",-> 음량의 차이가 심한 경우 레벨을 평준화 시키는 것.
Strategy for normalizing audio. Allowed values:loudness, clip, peak, rms
"classifier_free_guidance": 3

'''

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ai_notation.models import Ai_Info_Serializer,client_ai_info
from ai_notation.utils import transfer_json
from ai_notation import ai_create
from notation.transfet_utils import down_mp3,mp3_to_midi,transfer

@csrf_exempt
def get_ai_info(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =Ai_Info_Serializer(data=data)
        if serializer.is_valid():
            instance=serializer.save()
            # 인스턴스를 그대로 보내서 ai음악을 만드는 프로세스 돌리기
            ai_music_path=ai_create.create_ai_music_process(instance)
            if ai_music_path!=None:
                #스프링과 통신할 함수로 넘겨주기
                return export_to_spring(ai_music_path)
        return JsonResponse(serializer.errors, status=400)
    # else:
    #     return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)


# views.py in Django
from django.http import JsonResponse
import requests
import json,os
from django.http import HttpResponse
#down 저장소에있는 모든 파일 삭제 라이브러리
from notation.utils import delete
from django.conf import settings
#전역변수 관련 라이브러리
from base import BASIC_PATH,AUDIO_DOWN_PATH
from django.http import FileResponse
from django.contrib.staticfiles import finders
#스프링으로 전달하는 함수(pdf 전달)
def export_to_spring(pdf_path):
    print(pdf_path)
    # MusicXML 파일이 저장된 디렉토리 경로
    musicxml_directory = pdf_path
    try:
        with open(pdf_path, 'rb') as pdf_file:
                pdf_content = pdf_file.read()

        response = HttpResponse(content=pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{pdf_path.split("/")[-1]}"'
        return response
    except:
        return JsonResponse({'error': 'pdf변환 실패'}, status=405)
    # finally:
    # #down저장소에있는 모든 파일 삭제
    #     delete.delete_all_files_in_folder(AUDIO_DOWN_PATH)







    # # 가상의 데이터 생성 (실제 데이터 사용)
    # muscixml_path=muscixml_path
    # data_to_export = {'musicxmlfile': muscixml_path}

    # # JSON 파일 생성
    # json_data = json.dumps(data_to_export)

    # # 스프링 서버 URL
    # spring_url = 'http://spring-server-url/api/import-data'

    # # HTTP POST 요청을 통해 JSON 파일 전송
    # response = requests.post(spring_url, json=json_data, headers={'Content-Type': 'application/json'})

    # # 스프링에서의 응답 확인
    # spring_response = response.json()

    # # 장고에서의 응답
    # return JsonResponse({'django_response': 'Export successful', 'spring_response': spring_response})

