from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.conf import settings
#전역변수 관련 라이브러리
from base import BASIC_PATH,AUDIO_DOWN_PATH,AUDIO_MIDI_FILE

from notation.transfet_utils import down_mp3,mp3_to_midi,midi_to_xml,xml_to_pdf

def transfer_process(url,account_file_name):
    try:
        # mp3생성
        audio_path=down_mp3.download_audio(url)
        print('audio path',audio_path)
        # mp3-> midi
        midi_path=mp3_to_midi.down_musicxml(audio_path,AUDIO_DOWN_PATH,AUDIO_MIDI_FILE)
        print('midipath',midi_path)
        # midi->xml
        output_musicxml_file = AUDIO_DOWN_PATH+'\\audio.musicxml'
        musicxml_path=midi_to_xml.midi_to_musicxml(midi_path,output_musicxml_file)
        print(musicxml_path)
        # xml->pdf
        print('pdf로 바꾸나요')
        out_pdf_path=xml_to_pdf.convert_pdf(musicxml_path,AUDIO_DOWN_PATH)
    except:
        return JsonResponse({'error': 'pdf파일로 변환중 문제입니다. 서버문제 입니다'}, status=500)


    return out_pdf_path