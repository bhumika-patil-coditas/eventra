import jwt
import pem
from fastapi import Header
from src.constants import RolesEnum
from src.core import SETTINGS, CustomException
from src.schema import TokenPayload


class Auth:
    _public_key = None

    @classmethod
    def _get_public_key(cls):
        if cls._public_key is None:
            key = pem.parse_file(SETTINGS.PUBLIC_KEY_FILEPATH)
            cls._public_key = str(key[0]).encode()

        return cls._public_key

    @classmethod
    def verify_token(cls, token: str) -> TokenPayload:
        payload = jwt.decode(
            jwt=token,
            key=cls._get_public_key(),
            algorithms=["HS512"],
        )
        return TokenPayload.model_validate(payload)

    @classmethod
    def verify_hs_token(cls, token: str) -> TokenPayload:
        payload = jwt.decode(
            jwt=token,
            key=SETTINGS.PRIVATE_KEY_FOR_HS,
            algorithms=["HS384"],
        )
        return TokenPayload.model_validate(payload)

    @classmethod
    def RBAC(cls, allowed_roles: list[RolesEnum] | None = None):

        def check_rbac(Authorization: str = Header(...)):
            try:
                scheme, token = Authorization.split(" ", 1)
            except ValueError:
                raise CustomException.UnauthorizedError(
                    message="Invalid Authorization header."
                )

            if scheme.lower() != "bearer":
                raise CustomException.UnauthorizedError(
                    message="Invalid authentication scheme."
                )

            payload = cls.verify_hs_token(token)

            if not allowed_roles or payload.role in allowed_roles:
                return payload

            raise CustomException.ForbiddenError(
                message="You are not allowed to access this service."
            )

        return check_rbac