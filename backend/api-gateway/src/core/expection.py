from fastapi import HTTPException, status

class CustomException:

    @staticmethod
    def NotFoundError(resource: str = "Resource", resource_id=None, message: str | None = None) -> HTTPException:
        detail = message or f"{resource} not found."
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    @staticmethod
    def ConflictError(resource: object = None, message: str = "Conflict") -> HTTPException:
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=message)

    @staticmethod
    def UnauthorizedError(message: str = "Unauthorized") -> HTTPException:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message)

    @staticmethod
    def ForbiddenError(message: str = "Forbidden") -> HTTPException:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=message)

    @staticmethod
    def ValidationError(message: str = "Validation error") -> HTTPException:
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=message)

    @staticmethod
    def InternalError(message: str = "Internal server error") -> HTTPException:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message)
