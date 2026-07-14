from pydantic import BaseModel, EmailStr
from src.constants import RolesEnum

class GenerateOtpScema(BaseModel):
    email:str

class SendOtpResponse(BaseModel):
    otp: str
    expiration_in_milliSeconds: int

class SesOtpMailRequest(BaseModel):
    otp: str
    reciver_mail: EmailStr
    expire_in_min: int

class VerifyOtpRequest(BaseModel):
    code :str
    email: EmailStr

class TokenPayload(BaseModel):
    sub: str
    role: RolesEnum
    username: str