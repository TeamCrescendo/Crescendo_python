# # from django.test import TestCase
# import replicate
# import os
# import requests


# #Set the REPLICATE_API_TOKEN environment variable
# # os.environ["REPLICATE_API_TOKEN"] = "r8_PtWTfLOHWAJE91IrUeCiu9L8u2pnupC21PF1P"


# #     #ai로 음악 생성하는 함수
# # output = replicate.run(
# #     "meta/musicgen:b05b1dff1d8c6dc63d14b0cdb42135378dcb87f6373b0d3d341ede46e59e2b38",
# #     input={
# #         "top_k": 250,
# #         "top_p": 0,
# #         "prompt": "봄의 산뜻한 느낌을 담음 음악을 만들어줘",
# #         "duration": 10,
# #         "temperature": 1,
# #         "continuation": False,
# #         "model_version": "stereo-large",
# #         "output_format": "mp3",
# #         "continuation_start": 0,
# #         "multi_band_diffusion": False,
# #         "normalization_strategy": "peak",
# #         "classifier_free_guidance": 3
# #     }
# # )

# #생성된 mp3음악을 다운받는 프로세스
# url=output
# output_filename='output.mp3'
# response = requests.get(url)
# output_directory = "D:\\Crescendo_python\\download"
# output_path = os.path.join(output_directory, output_filename)

# with open(output_path, 'wb') as file:
#     file.write(response.content)

# print(f"{output_filename} 다운로드 완료.")

#midi파일로 변환해서 다운받는 프로세스
from basic_pitch.inference import predict_and_save
import os
from django.conf import settings
#전역변수 관련 라이브러리

# def down_musicxml(mp3_path):
#     predict_and_save(
#         [mp3_path],
#     'D:\\Crescendo_python\\download',
#         True,
#         True,
#         False,
#         False,
#     )
#     return 'D:\\Crescendo_python\\download'+'\\audio_basic_pitch.mid'

# down_musicxml('D:\\Crescendo_python\\download\\music.wav')


# from music21 import converter,instrument,note

# def midi_to_musicxml(input_midi,output_musicxml_path):
#     # MIDI 파일을 Music21 스트림으로 변환
#     midi_stream = converter.parse(input_midi)

#     #모든 악기를 피아노로 변경
#     # 모든 악기를 피아노로 변경
#     # for part in midi_stream.parts:
#     #     part.insert(0, instrument.Piano())
    
#     # for element in midi_stream.flat.notes:
#     #     if isinstance(element, note.Note):
#     #         element.quarterLength *= 1.5


#     # MusicXML 파일로 저장
#     midi_stream.write('musicxml', fp=output_musicxml_path)
#     return output_musicxml_path
# midi_to_musicxml('D:\\Crescendo_python\\download\\music_basic_pitch.mid','D:\\Crescendo_python\\download\\mu.music.xml')






# 환경 변수에서 MuseScore 실행 파일 경로 가져오기


# print(env)


# MUSESCORE_EXECUTABLE
import os
from music21 import converter, stream,environment
us = environment.UserSettings()
us['musicxmlPath'] = 'C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe'
us['musescoreDirectPNGPath'] = 'C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe'
us['musicxmlPath']

import subprocess

# MuseScore를 사용하여 MusicXML을 PDF로 변환
mscore_executable_path = 'C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe'
output_pdf_path = 'D:\\DEV\\Crescendo_python\\download\\output.pdf'
subprocess.run([mscore_executable_path, 'D:\\DEV\\Crescendo_python\\download\\audio.musicxml', '-o', output_pdf_path])