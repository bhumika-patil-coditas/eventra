from pydantic import BaseModel

class GetPresignedUrl(BaseModel):
    key:str

class UplaodPresignedUrlResponse(BaseModel):
    uploadUrl:str