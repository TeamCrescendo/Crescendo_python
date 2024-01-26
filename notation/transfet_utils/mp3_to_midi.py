""" 스포티파이 라이브러리 이용해서 변환  """
""" 무조건  python 10 버전 """
"""  """

from basic_pitch.inference import predict_and_save
import os
from django.conf import settings
#전역변수 관련 라이브러리
from base import BASIC_PATH,AUDIO_DOWN_PATH
current_directory = os.getcwd()
print(current_directory)
mp3_file_path = os.path.join('D:\\Crescendo_python\\download', "audio.mp3")

# 성공
def down_musicxml(mp3_path,output_dir):
    predict_and_save(
        [mp3_path],
        output_dir,
        True,
        True,
        False,
        False,
    )
    return output_dir+'\\audio_basic_pitch.mid'
# down_musicxml(mp3_file_path)