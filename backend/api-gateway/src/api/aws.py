from fastapi import APIRouter, Depends
from src.service import Clients
from src.constants import ServiceEnum
from src.dependencies import Microservice
from src.schema import VerifyMailRequest, GetObjectPresignedUrl

router = APIRouter(prefix="/aws", tags=["AWS"])

@router.post("/s3/get-uplaod-presigned-url")
def get_uplaod_presigned_url(key:str, service_dict:dict[ServiceEnum, Clients] = Depends(Microservice.get_service([ServiceEnum.AWS]))):
    return service_dict[ServiceEnum.AWS].call(request="get-upload-presigned-url", payload={"key" : key})

@router.post("/ses/verify-mail")
def verify_mail(data:VerifyMailRequest, service_dict:dict[ServiceEnum, Clients] = Depends(Microservice.get_service([ServiceEnum.AWS]))):
    return service_dict[ServiceEnum.AWS].call(request="verify-mail", payload=data.model_dump())

@router.get("/s3/get-object")
def get_object_presigned_url(data:GetObjectPresignedUrl, service_dict:dict[ServiceEnum, Clients] = Depends(Microservice.get_service([ServiceEnum.AWS]))):
    return service_dict[ServiceEnum.AWS].call(request="get-object", payload=data.model_dump(exclude_none=True))