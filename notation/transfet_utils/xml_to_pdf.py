import os
from music21 import converter, stream,environment

us = environment.UserSettings()
us['musicxmlPath'] = 'C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe'
us['musescoreDirectPNGPath'] = 'C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe'
us['musicxmlPath']



# MuseScore를 사용하여 MusicXML을 PDF로 변환

def convert_pdf(muscixml_path,output_dir):
    import subprocess
    print('들어오나요?')
    print(muscixml_path)
    mscore_executable_path = 'C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe'
    output_pdf_path = output_dir+'\\audio.pdf'
    subprocess.run([mscore_executable_path, muscixml_path, '-o', output_pdf_path])
    return output_pdf_path

# convert_pdf('D:\\DEV\\Crescendo_python\\download\\audio.musicxml')