import replicate
import os
import requests
from django.conf import settings
from django.http import JsonResponse
#전역변수 관련 라이브러리
from base import AI_AUDIO_DOWN_PATH
from notation.utils import delete
from notation.transfet_utils import mp3_to_midi,midi_to_xml,xml_to_pdf,make_dir,make_uuid
# replicate.set_token("r8_DJupDGbwmPN8TQzMJHw4OBO0Q11lEE64XX2Ub")
os.environ["REPLICATE_API_TOKEN"] = "r8_XzEp6Fk1nRDzVdgjt4PUIOjjSXK4lJq11wQ24"

def create_ai_music_process(data):
    account=data['account']
    prompt=data['prompt']
    duration=data['duration']
    print(account, prompt,duration)
    try:
        # 1. account 기반으로 dir 생성
        down_dir_path=make_dir.make_dir(account)
        #2. account 기반으로 uuid생성
        file_name=make_uuid.make_pk_file_name(account,'ai')
        # 3. prompt duratin 기반으로 ai 음악생성
        ai_mp3_path=create_ai_music_mp3(prompt,duration)
        # 4. ai 음악 다운로드
        mp3_path=ai_mp3_down(ai_mp3_path,down_dir_path,file_name)
        # mp3-> pdf
        out_pdf_path=transfer_mp3_to_pdf(mp3_path,down_dir_path,file_name)
    except:
        return JsonResponse({'error': 'pdf파일로 변환중 문제입니다. 서버문제 입니다'}, status=500)
    return out_pdf_path


def create_ai_music_mp3(prompt,duration):
    # Set the REPLICATE_API_TOKEN environment variable
    #ai로 음악 생성하는 함수
    print('들어오나요??')
    ai_output_path = replicate.run(
        "meta/musicgen:b05b1dff1d8c6dc63d14b0cdb42135378dcb87f6373b0d3d341ede46e59e2b38",
        input={
            "top_k": 250,
            "top_p": 0,
            "prompt": prompt,
            "duration": duration,
            "temperature": 1,
            "continuation": False,
            "model_version": "stereo-large",
            "output_format": "mp3",
            "continuation_start": 0,
            "multi_band_diffusion": False,
            "normalization_strategy": "peak",
            "classifier_free_guidance": 3
        }
    )

    return ai_output_path



def ai_mp3_down(ai_mp3_path,output_dir,file_name):
    output_filename=f'{file_name}.mp3'
    response = requests.get(ai_mp3_path)
    output_directory = output_dir
    output_path = os.path.join(output_directory, output_filename)

    with open(output_path, 'wb') as file:
        file.write(response.content)

    print(f"{output_path} 다운로드 완료.")
    return output_path


def transfer_mp3_to_pdf(mp3_path,output_dir,file_name):

    midi_path=mp3_to_midi.down_musicxml(mp3_path,output_dir,file_name)
    midi_file_path=f'{midi_path}_basic_pitch.mid'
    output_musicxml_file = output_dir+f'\\{file_name}.musicxml'
    musicxml_path=midi_to_xml.midi_to_musicxml(midi_file_path,output_musicxml_file)
    pdf_path=xml_to_pdf.convert_pdf(musicxml_path,output_dir,file_name)

    # delete.delete_files_in_folder(mp3_path)
    # delete.delete_files_in_folder(midi_path)
    # delete.delete_files_in_folder(musicxml_path)
    return pdf_path
# D:\DEV\Crescendo_python\download\member1\member1_ai_b61ec7d9-0fa1-4ac4-80a5-8cb8d874b54f.mp3
