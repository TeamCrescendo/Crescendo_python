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

   # output_directory='C:\\Dev\\Crescendo_python\\download'
    output_directory=AUDIO_DOWN_PATH
    print('다운받는 곳에서 url'+url)
    yt = YouTube(url)
    print('타이틀',yt.title)
    ys = yt.streams.filter(only_audio=True).first()
    video_output_path = os.path.join('C:\Crescendo_python\download', "audio")
    ys.download(output_path='C:\Crescendo_python\download', filename="audio")
    return video_output_path

#download_audio("https://www.youtube.com/watch?v=RdYVw7gBv14")



from pytube import YouTube
import os

def download_and_convert_to_mp3(video_url, output_path, output_filename="audio"):
    yt = YouTube(video_url)
    
    # 동영상 다운로드
    ys =  yt.streams.filter(only_audio=True).first()
    video_path = os.path.join(output_path, output_filename + ".mp4")
    ys.download(output_path=output_path, filename=output_filename)
    