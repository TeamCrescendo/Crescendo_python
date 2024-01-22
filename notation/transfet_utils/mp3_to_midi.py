""" 스포티파이 라이브러리 이용해서 변환  """
""" 무조건  python 10 버전 """
"""  """

from basic_pitch.inference import predict_and_save
import os
current_directory = os.getcwd()
print(current_directory)
mp3_file_path = os.path.join('D:\\Crescendo_python\\download', "audio.mp3")

# 성공
def down_musicxml(mp3_path):
    predict_and_save(
        [mp3_path],
        'D:\\Crescendo_python\\download',
        True,
        True,
        False,
        False,
    )
down_musicxml(mp3_file_path)