#midi파일을 json파일로 변환해서 리턴하는 함수

from music21 import converter,instrument,note

def midi_to_musicxml(input_midi,output_musicxml_path):
    # MIDI 파일을 Music21 스트림으로 변환
    midi_stream = converter.parse(input_midi)

    #모든 악기를 피아노로 변경
    # 모든 악기를 피아노로 변경
    # for part in midi_stream.parts:
    #     part.insert(0, instrument.Piano())
    
    # for element in midi_stream.flat.notes:
    #     if isinstance(element, note.Note):
    #         element.quarterLength *= 1.5


    # MusicXML 파일로 저장
    midi_stream.write('musicxml', fp=output_musicxml_path)
    return output_musicxml_path

# MIDI 파일 경로와 MusicXML 파일 경로를 지정
# input_midi_file = 'D:\\Crescendo_python\\download\\audio_bacic_pitch.mid'
# output_musicxml_file = 'D:\\Crescendo_python\\download\\audio.musicxml'

# MIDI를 MusicXML로 변환
# midi_to_musicxml(input_midi_file, output_musicxml_file)
