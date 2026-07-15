from pydantic import BaseModel, EmailStr
from typing import Optional
class VerifyMailRequest(BaseModel):
    email:EmailStr

class GetObjectPresignedUrl(BaseModel):
    key : str
    exp_in_sec: Optional[int] = None