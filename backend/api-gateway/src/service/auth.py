import pem
from src.core import SETTINGS, CustomException
import jwt
from src.constants import RolesEnum
from fastapi import Header
from src.schema import TokenPayload


class Auth:
    
    @classmethod
    def verify_token(cls, token:str) -> TokenPayload:
        try:
            private_key = pem.parse_file(SETTINGS.PUBLIC_KEY_FILEPATH)
            secret_key_pem = bytes(str(private_key[0]), 'utf-8')

            data = jwt.decode(jwt=token, key=secret_key_pem, algorithms=["HS512"])

            return TokenPayload.model_validate(data)
        except Exception:
            raise
    

    @classmethod
    def RBAC(cls, allowed_roles:list[RolesEnum] = []):
        
        def check_rbac(Authorization:str = Header(...)):

            token:str = Authorization.split(" ")[-1]
            payload:TokenPayload = cls.verify_token(token = token)

            #only authentation.
            if allowed_roles is None or allowed_roles == []:
                return payload

            elif payload.role in allowed_roles:
                return payload
            else:
                raise CustomException.ForbiddenError(message="You are not allowed to access this service.")

        return check_rbac