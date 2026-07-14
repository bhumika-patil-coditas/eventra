from fastapi import APIRouter, Depends
from src.dependencies import deps
from src.service import S3service
from uuid import UUID
from typing import Optional

router = APIRouter(prefix="/s3", tags=["S3"])

@router.get("/get-object")
def get_s3_object(aws_key:str, exp_in_sec:Optional[int]=None, s3_service:S3service = Depends(deps.get_s3_service)):
    if exp_in_sec:
        return s3_service.generate_get_presigned_url(aws_key=aws_key, exp=exp_in_sec)
    return s3_service.generate_get_presigned_url(aws_key=aws_key)

@router.post("/vendor-galary/get-presigened-url")
def get_presigned_for_vendor_photo(vendor_id:UUID, file_name:str, s3_service:S3service = Depends(deps.get_s3_service)):
    key = f"{vendor_id}/{UUID().hex}-{file_name}"
    return s3_service.generate_upload_presigned_url(aws_key=key)

