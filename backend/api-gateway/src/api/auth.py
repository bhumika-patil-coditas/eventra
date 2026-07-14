from fastapi import APIRouter, Depends
from src.schema import GenerateOtpScema,SendOtpResponse, SesOtpMailRequest, VerifyOtpRequest
from src.service.clients import Clients
from src.constants import ServiceEnum
from src.dependencies import Microservice


router = APIRouter(prefix ="/auth", tags=["auth"])

@router.post("/generate-otp")
def generate_otp(data:GenerateOtpScema, service_dict:dict[ServiceEnum, Clients] = Depends(Microservice.get_service([ServiceEnum.AUTH, ServiceEnum.AWS]))):

    otp_response = service_dict[ServiceEnum.AUTH].call(request="generate-otp", payload=data.model_dump())
    otp_response_model = SendOtpResponse.model_validate(otp_response)

    ses_payload = SesOtpMailRequest(otp=otp_response_model.otp , reciver_mail= data.email , expire_in_min=otp_response_model.expiration_in_milliSeconds//(1000*60))
    response = service_dict[ServiceEnum.AWS].call(request="send_otp", payload = ses_payload.model_dump())

    return "Otp send sucessfully."

@router.post("/verify-otp")
def verify_otp(data:VerifyOtpRequest,  service_dict:dict[ServiceEnum, Clients] = Depends(Microservice.get_service([ServiceEnum.AUTH]))):
    return service_dict[ServiceEnum.AUTH].call(request="verify-otp", payload=data.model_dump())





