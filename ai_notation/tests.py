# from django.test import TestCase
import replicate
import os
import requests


#Set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = "r8_PtWTfLOHWAJE91IrUeCiu9L8u2pnupC21PF1P"
output = replicate.run(
    "meta/musicgen:b05b1dff1d8c6dc63d14b0cdb42135378dcb87f6373b0d3d341ede46e59e2b38",
    input={
        "top_k": 250,
        "top_p": 0,
        "prompt": "Edo25 major g melodies that sound triumphant and cinematic. Leading up to a crescendo that resolves in a 9th harmonic",
        "duration": 7,
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


url=output
output_filename='output.mp3'
response = requests.get(url)
output_directory = "D:\\Crescendo_python\\download"
output_path = os.path.join(output_directory, output_filename)

with open(output_path, 'wb') as file:
    file.write(response.content)


print(f"{output_filename} 다운로드 완료.")


from basic_pitch.inference import predict_and_save
import os
from django.conf import settings
#전역변수 관련 라이브러리

def down_musicxml(mp3_path):
    predict_and_save(
        [mp3_path],
       'D:\\Crescendo_python\\download',
        True,
        True,
        False,
        False,
    )
    return 'D:\\Crescendo_python\\download'+'\\audio_basic_pitch.mid'

down_musicxml(output_path)