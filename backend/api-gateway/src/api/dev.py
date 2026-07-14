from fastapi import APIRouter, Depends
from src.schema import VerifyMailRequest
from src.service.clients import Clients
from src.constants import ServiceEnum
from src.dependencies import Microservice


router:APIRouter = APIRouter(prefix="/dev", tags=["dev"])

@router.post("/ses/verify-mail")
def verify_mail(data:VerifyMailRequest, service_dict:dict[ServiceEnum, Clients] = Depends(Microservice.get_service([ServiceEnum.AWS]))):
    return service_dict[ServiceEnum.AWS].call(request="verify-mail", payload=data.model_dump())

