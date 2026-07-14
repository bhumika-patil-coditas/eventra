from src.service import SesService, S3service


class Dependency:

    S3_SERVICE = S3service()
    SES_SERVICE = SesService()

    @classmethod
    def get_s3_service(cls)-> S3service:
        return cls.S3_SERVICE
    
    @classmethod
    def get_ses_service(cls) -> SesService:
        return cls.SES_SERVICE
    
deps = Dependency()
    
    