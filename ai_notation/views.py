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
from ai_notation.models import Ai_Info_Serializer,server_ai_info
from ai_notation.utils import transfer_json
from notation.transfet_utils import down_mp3,mp3_to_midi,transfer

@csrf_exempt
def get_ai_info(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =Ai_Info_Serializer(data=data)
        # JSON 파일을 받아오는데 성공하면
        if serializer.is_valid():
            instance=serializer.save()
            #ai처리시 필요한 정보가 전부들어있는 데이터파일
            server_data=server_ai_info(instance)
            #server_data를 json으로 변환하는 함수
            transfer_json.data_to_jaon(server_data)

            #ai로 음악을 생성하는 함수 -> mp3 path 반환하기
        
            #
            musicxml_path=transfer.transfer_process(instance.url)

            # 오류 없이 생성되서 muscixml_path가 None이 아니라면
            if musicxml_path!=None:
                #스프링과 통신할 함수로 넘겨주기
                return export_to_spring(musicxml_path)
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
#스프링으로 전달하는 함수
def export_to_spring(muscixml_path):
    print(muscixml_path)
    # MusicXML 파일이 저장된 디렉토리 경로
    musicxml_directory = muscixml_path

    # MusicXML 파일 이름 (예: example.musicxml)
    musicxml_filename = 'audio.musicxml'

    # MusicXML 파일의 전체 경로
    musicxml_path = musicxml_directory
    
    # os.path.join(musicxml_directory, musicxml_filename)

    try:
        # MusicXML 파일 열기
        with open(musicxml_path, 'rb') as musicxml_file:
            # 파일을 HttpResponse에 담아서 응답
            response = HttpResponse(musicxml_file.read(), content_type='application/xml')
            response['Content-Disposition'] = f'attachment; filename="{musicxml_filename}"'

            
            return response

    except FileNotFoundError:
        return HttpResponse('MusicXML file not found', status=404)
    # finally:
    #     #down저장소에있는 모든 파일 삭제
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

