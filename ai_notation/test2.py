#python-> json 테스트
import json

# 파이썬 데이터 예시 (딕셔너리)
python_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# 파이썬 데이터를 JSON 문자열로 변환
json_data = json.dumps(python_data)

print(json_data)
