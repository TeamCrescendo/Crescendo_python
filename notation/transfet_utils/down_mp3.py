# from rest_framework.views import APIView
# from rest_framework.response import Response
import os
from pytube import YouTube
from django.conf import settings
#전역변수 관련 라이브러리
from base import BASIC_PATH,AUDIO_DOWN_PATH

# 유튜브 url이 오면 mp3로 바꿔줌
# 경로 수정하기
def download_audio(url):
    #왜안됨..
    #url=url
   # output_directory='C:\\Dev\\Crescendo_python\\download'
    output_directory=AUDIO_DOWN_PATH
    yt = YouTube(url)
    ys = yt.streams.filter(only_audio=True).first()
    video_output_path = os.path.join(output_directory, "audio.mp3")
    ys.download(output_path=output_directory, filename="audio.mp3")
    return video_output_path

# download_audio("https://www.youtube.com/watch?v=RdYVw7gBv14")