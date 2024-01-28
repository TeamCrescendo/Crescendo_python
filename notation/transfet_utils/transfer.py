from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.conf import settings
#전역변수 관련 라이브러리

from notation.utils import delete
from notation.transfet_utils import down_mp3,mp3_to_midi,midi_to_xml,xml_to_pdf,make_dir,make_uuid
def transfer_process(url,account):
    try:
        #account기반으로 dir생성
        down_dir_path=make_dir.make_dir(account)
        #account 기반으로 uuid생성
        file_name=make_uuid.make_pk_file_name(account)
        #youtube Link->pdf 
        out_pdf_path=transfer_link_to_pdf(url,down_dir_path,file_name)
    except:
        return JsonResponse({'error': 'pdf파일로 변환중 문제입니다. 서버문제 입니다'}, status=500)


    return out_pdf_path



def transfer_link_to_pdf(url,down_dir_path,file_name):
        
        # mp3생성
        audio_path=down_mp3.download_audio(url,file_name,down_dir_path)
        print('audio path',audio_path)
        # mp3-> midi
        midi_file_name=f'{file_name}_basic_pitch.mid'
        midi_path=mp3_to_midi.down_musicxml(audio_path,down_dir_path,midi_file_name)
        print('midipath',midi_path)
        
        # midi->xml
        output_musicxml_file = down_dir_path+f'\\{file_name}.musicxml'
        print(output_musicxml_file)
        musicxml_path=midi_to_xml.midi_to_musicxml(midi_path,output_musicxml_file)
        print(musicxml_path)

        # xml->pdf
        print('pdf로 바꾸나요')
        out_pdf_path=xml_to_pdf.convert_pdf(musicxml_path,down_dir_path,file_name)

        delete.delete_files_in_folder(audio_path)
        delete.delete_files_in_folder(midi_path)
        delete.delete_files_in_folder(musicxml_path)
        return out_pdf_path

