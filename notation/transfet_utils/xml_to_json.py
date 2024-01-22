from music21 import converter, stream, note, chord
import json

def extract_note_data(music21_object):
    if isinstance(music21_object, note.Note):
        return {
            "pitch": str(music21_object.pitch),
            "duration": float(music21_object.duration.quarterLength),
            "offset": float(music21_object.offset),
            "octave": music21_object.pitch.octave,
        }
    elif isinstance(music21_object, chord.Chord):
        return [
            {
                "pitch": str(single_pitch),
                "duration": float(music21_object.duration.quarterLength),
                "offset": float(music21_object.offset),
                "octave": single_pitch.octave,
            }
            for single_pitch in music21_object.pitches
        ]
    else:
        return None

def musicxml_to_json(input_musicxml, output_json):
    # MusicXML 파일을 Music21 스트림으로 변환
    musicxml_stream = converter.parse(input_musicxml)

    # JSON 파일에 저장할 데이터 리스트 초기화
    json_data = []

    # 각 Part의 Note 정보를 추출하여 리스트에 추가
    for part in musicxml_stream.parts:
        part_data = []
        for music21_object in part.flat.notesAndRests:
            note_data = extract_note_data(music21_object)
            if note_data:
                part_data.extend(note_data)

        # Part 데이터를 전체 리스트에 추가
        json_data.append(part_data)

    # JSON 파일로 저장
    with open(output_json, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

# MusicXML 파일 경로와 JSON 파일 경로를 지정
input_musicxml_file = 'D:\\Crescendo_python\\download\\audio.musicxml'
output_json_file = 'D:\\Crescendo_python\\download\\audio.json'

# MusicXML을 JSON으로 변환
musicxml_to_json(input_musicxml_file, output_json_file)
