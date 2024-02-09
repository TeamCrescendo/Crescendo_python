
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
AUDIO_MIDI_FILE='basic_pitch.mid'

AI_AUDIO_DOWN_PATH=BASIC_PATH+'\\ai_download'
MUSESCORE_EXECUTABLE='C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe'
AWS_END_POINT='https:\\spring-todo-api-bucket-seon.s3.ap-northeast-2.amazonaws.com\\'
AWS_BUCKET_NAME='spring-todo-api-bucket-seon'
AWS_ACCESS_KEY_ID ="AKIA3FLD5HZYURZGWSOA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_DEFAULT_REGION = "ap-northeast-2"
# ... 기타 설정을 필요에 따라 상속
