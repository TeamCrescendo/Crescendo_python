import os
from django.conf import settings
#전역변수 관련 라이브러리
from base import BASIC_PATH,AUDIO_DOWN_PATH
def delete_all_files_in_folder(AUDIO_DOWN_PATH):
    print('이거 돌아감..?')
    try:
        # 폴더 내 모든 파일 가져오기
        files = os.listdir(AUDIO_DOWN_PATH)

        # 각 파일을 삭제
        for file in files:
            file_path = os.path.join(AUDIO_DOWN_PATH, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{file_path} deleted")

        print("All files deleted successfully.")

    except Exception as e:
        print(f"Error: {e}")

