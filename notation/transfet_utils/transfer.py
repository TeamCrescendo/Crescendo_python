from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser



from down_mp3 import download_audio
from mp3_to_midi import down_musicxml
from midi_to_xml import midi_to_musicxml

def transfer_process(url):
    # 과정마다 에러나면 badrequest보내기
    #mp3다운중 에러 -> 유트브 정책상문제로 다운로드 할수 없습니다..
    #midi파일 다운중 에러-> midi파일로 변환중 문제입니다. 다시한번 시도해주세요!
    #xml 변환중 에러-> xml파일 다운중에러입니다. 다시한번 시도해주세요!
    try:
        audio_path=download_audio(url)
    except:
        return JsonResponse({'error': '유트브 정책상문제로 다운로드 할수 없습니다. 다른 음원을 이용해보세요!'}, status=405)
    
    try:
        midi_path=down_musicxml(audio_path)
    except:
        return JsonResponse({'error': 'midi파일로 변환중 문제입니다. 서버문제 입니다'}, status=500)
    
    try:
        musicxml_path=midi_to_musicxml(midi_path)
    except:
        return JsonResponse({'error': 'midi파일로 변환중 문제입니다. 서버문제 입니다'}, status=500)
    
    return musicxml_path
