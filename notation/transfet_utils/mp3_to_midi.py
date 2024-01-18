""" 스포티파이 라이브러리 이용해서 변환  """
""" 무조건  python 10 버전 """
"""  """

from basic_pitch.inference import predict_and_save
import os
current_directory = os.getcwd()
print(current_directory)
# MP3 파일을 WAV 파일로 변환
mp3_file_path = os.path.join(current_directory, "audio.mp3")

# 성공
predict_and_save(
    [mp3_file_path],
    current_directory,
    True,
    True,
    False,
    False,
)