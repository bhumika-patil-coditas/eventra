from fastapi import APIRouter, Depends

from src.constants import ServiceEnum
from src.dependencies import Microservice
from src.schema import (
    GenerateOtpScema,
    SendOtpResponse,
    SesOtpMailRequest,
    VerifyOtpRequest,
    TokenPayload,
)
from src.service import Auth, Clients


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/generate-otp")
def generate_otp(
    data: GenerateOtpScema,
    services: dict[ServiceEnum, Clients] = Depends(
        Microservice.get_service([ServiceEnum.AUTH, ServiceEnum.AWS])
    ),
):
    auth_client = services[ServiceEnum.AUTH]
    aws_client = services[ServiceEnum.AWS]

    otp = SendOtpResponse.model_validate(
        auth_client.call(
            request="generate-otp",
            payload=data.model_dump(),
        )
    )

    aws_client.call(
        request="send_otp",
        payload=SesOtpMailRequest(
            otp=otp.otp,
            reciver_mail=data.email,
            expire_in_min=otp.expiration_in_milliSeconds // (1000 * 60),
        ).model_dump(),
    )

    return {"message": "OTP sent successfully."}


@router.post("/verify-otp")
def verify_otp(
    data: VerifyOtpRequest,
    services: dict[ServiceEnum, Clients] = Depends(
        Microservice.get_service([ServiceEnum.AUTH])
    ),
):
    return services[ServiceEnum.AUTH].call(
        request="verify-otp",
        payload=data.model_dump(),
    )


@router.get("/me")
def get_me(
    user: TokenPayload = Depends(Auth.RBAC()),
):
    return user