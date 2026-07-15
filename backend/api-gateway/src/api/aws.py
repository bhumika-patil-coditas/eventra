from fastapi import APIRouter, Depends

from src.constants import ServiceEnum
from src.dependencies import Microservice
from src.schema import GetObjectPresignedUrl, VerifyMailRequest
from src.service import Clients


router = APIRouter(prefix="/aws", tags=["AWS"])


@router.post("/s3/get-upload-presigned-url")
def get_upload_presigned_url(
    key: str,
    services: dict[ServiceEnum, Clients] = Depends(
        Microservice.get_service([ServiceEnum.AWS])
    ),
):
    aws = services[ServiceEnum.AWS]

    return aws.call(
        request="get-upload-presigned-url",
        payload={"key": key},
    )


@router.post("/ses/verify-mail")
def verify_mail(
    data: VerifyMailRequest,
    services: dict[ServiceEnum, Clients] = Depends(
        Microservice.get_service([ServiceEnum.AWS])
    ),
):
    aws = services[ServiceEnum.AWS]

    return aws.call(
        request="verify-mail",
        payload=data.model_dump(),
    )


@router.get("/s3/get-object")
def get_object_presigned_url(
    data: GetObjectPresignedUrl,
    services: dict[ServiceEnum, Clients] = Depends(
        Microservice.get_service([ServiceEnum.AWS])
    ),
):
    aws = services[ServiceEnum.AWS]

    return aws.call(
        request="get-object",
        payload=data.model_dump(exclude_none=True),
    )