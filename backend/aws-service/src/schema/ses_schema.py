from pydantic import BaseModel, EmailStr

class OtpMailRequest(BaseModel):
    otp: str
    reciver_mail: EmailStr
    expire_in_min: int

class VerifyMailRequest(BaseModel):
    email:EmailStr