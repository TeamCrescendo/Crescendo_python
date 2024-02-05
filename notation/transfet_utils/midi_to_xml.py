#midi파일을 json파일로 변환해서 리턴하는 함수

from music21 import converter,instrument,note,stream

def midi_to_musicxml(input_midi,output_musicxml_path,title):
    print('xml 변환으로 들어오나요?')
    # MIDI 파일을 Music21 스트림으로 변환
    print('midi패스 -->',input_midi)
    midi_stream = converter.parse(input_midi)
    
    # MusicXml:이름, 작곡가 변경
    print(len(title))
    new_title=''
    if len(title)>=10:
        new_title+=title[0:10]+'\n'
        new_title+=title[10:len(title)]+'\n'
    midi_stream.metadata.title = new_title
    midi_stream.metadata.composer="Creseondo"
    # MusicXML 파일로 저장
    midi_stream.write('musicxml', fp=output_musicxml_path)
    return output_musicxml_path

# MIDI 파일 경로와 MusicXML 파일 경로를 지정
# input_midi_file = 'D:\\Crescendo_python\\download\\audio_bacic_pitch.mid'
# output_musicxml_file = 'D:\\Crescendo_python\\download\\audio.musicxml'

# MIDI를 MusicXML로 변환
# midi_to_musicxml(input_midi_file, output_musicxml_file)
