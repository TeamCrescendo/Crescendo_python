import os
from django.conf import settings
import shutil
#전역변수 관련 라이브러리
from aws_base import BASIC_PATH,AUDIO_DOWN_PATH
def delete_files_in_folder(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.remove(file_path)
                print("Deleted file:", file_path)
            except Exception as e:
                print("Failed to delete file:", file_path, "Error:", e)
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                shutil.rmtree(dir_path)
                print("Deleted directory:", dir_path)
            except Exception as e:
                print("Failed to delete directory:", dir_path, "Error:", e)

        print("All files deleted successfully.")

    # except Exception as e:
    #     print(f"Error: {e}")

