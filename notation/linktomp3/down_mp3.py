from rest_framework.views import APIView
from rest_framework.response import Response
import os
from pytube import YouTube

class MyApiView(APIView):
    def download_audio():
        url='https://www.youtube.com/watch?v=qRdTyoZd3rg'
        output_directory='C:\\'
        yt = YouTube(url)
        ys = yt.streams.filter(only_audio=False).first()
        video_output_path = os.path.join(output_directory, "audio.mp3")
        ys.download(output_path=output_directory, filename="audio.mp3")
        return video_output_path
    