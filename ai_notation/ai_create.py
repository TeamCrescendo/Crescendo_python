import replicate
import os
import requests
from django.conf import settings
#전역변수 관련 라이브러리
from base import AI_AUDIO_DOWN_PATH
from notation.transfet_utils import mp3_to_midi,midi_to_xml,xml_to_pdf
# replicate.set_token("r8_DJupDGbwmPN8TQzMJHw4OBO0Q11lEE64XX2Ub")
os.environ["REPLICATE_API_TOKEN"] = "r8_DJupDGbwmPN8TQzMJHw4OBO0Q11lEE64XX2Ub"

def create_ai_music_process(instance):
    prompt=instance.prompt
    duration=instance.duration
    ai_mp3_path=create_ai_music_mp3(prompt,duration)
    mp3_path=ai_mp3_down(ai_mp3_path)
    midi_path=mp3_to_midi.down_musicxml(mp3_path,AI_AUDIO_DOWN_PATH)
    xml_path=midi_to_xml.midi_to_musicxml(midi_path,AI_AUDIO_DOWN_PATH+'ai.musicxml')
    pdf_path=xml_to_pdf.convert_pdf(xml_path,AI_AUDIO_DOWN_PATH)
    return pdf_path


def create_ai_music_mp3(prompt,duration):
    # Set the REPLICATE_API_TOKEN environment variable
    

    #ai로 음악 생성하는 함수
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



def ai_mp3_down(ai_mp3_path):
    output_filename='ai_output.mp3'
    response = requests.get(ai_mp3_path)
    output_directory = AI_AUDIO_DOWN_PATH
    output_path = os.path.join(output_directory, output_filename)

    with open(output_path, 'wb') as file:
        file.write(response.content)

    print(f"{output_filename} 다운로드 완료.")
    return output_path