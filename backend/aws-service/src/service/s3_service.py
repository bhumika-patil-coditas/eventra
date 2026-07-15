import boto3
from botocore.exceptions import ClientError
from src.core import SETTINGS, CustomException, LOGGER
from fastapi import UploadFile
from uuid import uuid4
from pathlib import Path
import os
from src.schema import UplaodPresignedUrlResponse

class S3service:

    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            region_name=SETTINGS.AWS_REGION,
            aws_access_key_id=SETTINGS.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=SETTINGS.AWS_SECRET_ACCESS_KEY,
        )
    
    async def save_to_s3(self, file:UploadFile):
            
        content = await file.read()
        key = f"{str(uuid4())}.{file.filename.split(".")[-1]}"
        file_path = Path("tmp" ,key )
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(content)
        try:
            response = self.s3_client.upload_file(file_path, SETTINGS.S3_BUCKET_NAME, key)
        except ClientError as e:
            LOGGER.error(e)
            raise CustomException.InternalError(message="Error connecting to s3.")
        LOGGER.info(response)
        os.remove(file_path)
        return key
    
    def generate_upload_presigned_url(self, aws_key:str, exp:int = 5*24*60*60):
        try:
            response = self.s3_client.generate_presigned_url(
                'put_object',
                Params={'Bucket': SETTINGS.S3_BUCKET_NAME, 'Key': aws_key},
                ExpiresIn=exp,
            )
            return UplaodPresignedUrlResponse(uploadUrl=response)
        except ClientError as e:
            LOGGER.error(e)
            raise CustomException.InternalError(message="Error connecting to s3.")
    
    def generate_get_presigned_url(self, aws_key:str, exp:int = 5*24*60*60):
        try:
            response = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': SETTINGS.S3_BUCKET_NAME, 'Key': aws_key},
                ExpiresIn=exp,
            )
            return response
        except ClientError as error:
            if error.response['ResponseMetadata']['HTTPStatusCode'] == 404:
                LOGGER.info('No object found - File has been moved')
            else:
                raise error
