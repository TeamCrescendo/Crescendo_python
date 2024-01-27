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
from notation.transfet_utils import down_mp3,mp3_to_midi,transfer

@csrf_exempt
def get_youtube_info(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # serializer =Youtube_Info_Serializer(data=data)
        # JSON 파일을 받아오는데 성공하면
        if data!=None:
            # instance=serializer.save() ->db에 저장하는 거라 쓸모없음
            print(data['account'])
            # print(serializer)
            # json_data=JsonResponse(serializer.data, status=201)
            #mp3파일 다운받고 midi파일로 변환-> MUSICXML 파일로 변환하는 프로세스 함수
            url=data['url']
            account_file_name=data['account']
            pdf_path=transfer.transfer_process(url,account_file_name)

            # 오류 없이 생성되서 muscixml_path가 None이 아니라면
            if pdf_path!=None:
                #스프링과 통신할 함수로 넘겨주기
                return export_to_spring(pdf_path)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)


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
        response['pdf_path'] = pdf_path
        return response
    except:
         return JsonResponse({'error': 'pdf변환 실패'}, status=405)
    # finally:
    #     #down저장소에있는 모든 파일 삭제
    #     delete.delete_all_files_in_folder(AUDIO_DOWN_PATH)

         




# musicxml 온전히 전달할 경우
    # try:
    #     # MusicXML 파일 열기
    #     with open(musicxml_path, 'rb') as musicxml_file:
    #         # 파일을 HttpResponse에 담아서 응답
    #         response = HttpResponse(musicxml_file.read(), content_type='application/xml')
    #         response['Content-Disposition'] = f'attachment; filename="{musicxml_filename}"'

            
    #         return response

    # except FileNotFoundError:
    #     return HttpResponse('MusicXML file not found', status=404)
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

