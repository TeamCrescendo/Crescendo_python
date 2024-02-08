import logging
import boto3
from botocore.exceptions import ClientError
from base import AWS_ACCESS_KEY_ID,AWS_BUCKET_NAME,AWS_DEFAULT_REGION,AWS_END_POINT,AWS_SECRET_ACCESS_KEY

# s3 = boto3.client('s3')
# response = s3.list_buckets() # bucket 목록
# print(response)
# python 연결

s3_client = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_DEFAULT_REGION
                      )


#  s3 업로드
def uploadRoS3Bucket(account,local_file_path,file_name):

    object_name=account+'/'
    s3_client.put_object(Bucket=AWS_BUCKET_NAME,Key=object_name)

    # 자고싶다
    #uploadFile
    s3_client.upload_file(local_file_path, AWS_BUCKET_NAME, object_name+file_name)
    print('업로드 완료')
    return AWS_END_POINT+object_name+file_name

# uploadRoS3Bucket('member1','D:\\DEV\\Crescendo_python\\aws_tool\\1000000285.jpg','ttt2.jpg')

    

# response = client.list_buckets() # bucket 목록
# for bucket in response.get('Buckets', []):
#     print (bucket.get('Name'))