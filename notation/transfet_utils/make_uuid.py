# pdf를 구별하기위 uuid를 만드는 함수
# 반환값 account_uuid
import uuid
def make_pk_file_name(account,create_method='youtube'):
    # 랜덤 UUID 생성
    random_uuid = uuid.uuid4()

    # UUID 문자열로 변환
    uuid_string = str(random_uuid)
    if create_method=='youtube':
        file_name=f'{account}_{uuid_string}'
    else:
        file_name=f'{account}_ai_{uuid_string}'

    return file_name
