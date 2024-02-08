# account별 폴더를 만드는 함수
#  존재하면 그대로 쓰고 아니면 폴더만들기

from django.conf import settings
#전역변수 관련 라이브러리
from aws_base import BASIC_PATH,AUDIO_DOWN_PATH
import os

def make_dir(account):
    directory_path=os.path.join(AUDIO_DOWN_PATH, account)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    return directory_path