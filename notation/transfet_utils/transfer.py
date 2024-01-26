from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.conf import settings
#전역변수 관련 라이브러리
from base import BASIC_PATH,AUDIO_DOWN_PATH,AUDIO_MIDI_FILE

from notation.transfet_utils import down_mp3,mp3_to_midi,midi_to_xml,xml_to_pdf

def transfer_process(url):
    print('url',url)
    # 과정마다 에러나면 badrequest보내기
    #mp3다운중 에러 -> 유트브 정책상문제로 다운로드 할수 없습니다..
    #midi파일 다운중 에러-> midi파일로 변환중 문제입니다. 다시한번 시도해주세요!
    #xml 변환중 에러-> xml파일 다운중에러입니다. 다시한번 시도해주세요!
    print('변환작업')
    try:

        audio_path=down_mp3.download_audio(url)
        # down_mp3.download_audio(url)
        print('audio path',audio_path)
    except:
        print('다운이 안받아져요')
    # JsonResponse({'error': '유트브 정책상문제로 다운로드 할수 없습니다. 다른 음원을 이용해보세요!'}, status=405)
    
    try:
        midi_path=mp3_to_midi.down_musicxml(audio_path,AUDIO_DOWN_PATH,AUDIO_MIDI_FILE)
        print('midipath',midi_path)
    except:
        return JsonResponse({'error': 'midi파일로 변환중 문제입니다. 서버문제 입니다'}, status=500)
    
    try:
        output_musicxml_file = AUDIO_DOWN_PATH+'\\audio.musicxml'
        musicxml_path=midi_to_xml.midi_to_musicxml(midi_path,output_musicxml_file)
        print(musicxml_path)
    except:
        return JsonResponse({'error': 'xml파일로 변환중 문제입니다. 서버문제 입니다'}, status=500)

    try:
        print('pdf로 바꾸나요')
        out_pdf_path=xml_to_pdf.convert_pdf(musicxml_path,AUDIO_DOWN_PATH)
    except:
        return JsonResponse({'error': 'pdf파일로 변환중 문제입니다. 서버문제 입니다'}, status=500)

    
    return out_pdf_path
