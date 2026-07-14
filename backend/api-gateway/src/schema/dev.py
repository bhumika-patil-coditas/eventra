from pydantic import BaseModel, EmailStr

class VerifyMailRequest(BaseModel):
    email:EmailStr