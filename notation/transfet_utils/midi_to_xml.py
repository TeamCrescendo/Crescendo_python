#midi파일을 json파일로 변환해서 리턴하는 함수

from music21 import converter

def midi_to_musicxml(input_midi,output_musicxml_path):
    # MIDI 파일을 Music21 스트림으로 변환
    midi_stream = converter.parse(input_midi)
    # MusicXML 파일로 저장
    midi_stream.write('musicxml', fp=output_musicxml_path)
    return output_musicxml_path

# MIDI 파일 경로와 MusicXML 파일 경로를 지정
# input_midi_file = 'D:\\Crescendo_python\\download\\audio_bacic_pitch.mid'
# output_musicxml_file = 'D:\\Crescendo_python\\download\\audio.musicxml'

# MIDI를 MusicXML로 변환
# midi_to_musicxml(input_midi_file, output_musicxml_file)
