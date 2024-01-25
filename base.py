# 전역적으로 사용할 사용자 정의 변수들을 저장하는 파일
# myproject/settings/base.py
import os
# Django의 기본 설정 가져오기
from django.conf import settings
# Django 기본 설정 상속
DATABASES = settings.DATABASES
DEBUG = settings.DEBUG

BASIC_PATH=os.getcwd()
AUDIO_DOWN_PATH=BASIC_PATH+'\\download'
AI_AUDIO_DOWN_PATH=BASIC_PATH+'\\ai_download'
MUSESCORE_EXECUTABLE='C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe'
# ... 기타 설정을 필요에 따라 상속
