from fastapi import APIRouter, Depends
from src.dependencies import deps
from src.service import SesService
from src.schema import OtpMailRequest


router = APIRouter(prefix="/ses", tags=["ses"])

@router.post("/send-otp")
def send_otp_mail(data:OtpMailRequest , ses_service:SesService = Depends(deps.get_ses_service)):
    sub= "Login OTP"
    body = (
        f"Hey {data.reciver_mail},\n"
        "\n"
        f"Welcome to the platform. here is your OTP : {data.otp}.\n"
        "\n"
        f"* This otp is valid for only {data.expire_in_min} minutes."

    )
    return ses_service.send_text_mail(to_address=[data.reciver_mail] , subject=sub, body_text=body)
