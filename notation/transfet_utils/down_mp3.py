from rest_framework.views import APIView
from rest_framework.response import Response
import os
from pytube import YouTube

# 유튜브 url이 오면 mp3로 바꿔줌
# 경로 수정하기
def download_audio(url):
    url=url
   # output_directory='C:\\Dev\\Crescendo_python\\download'
    output_directory='D:\\Crescendo_python\\download'
    yt = YouTube(url)
    ys = yt.streams.filter(only_audio=False).first()
    video_output_path = os.path.join(output_directory, "audio.mp3")
    ys.download(output_path=output_directory, filename="audio.mp3")
    return video_output_path
