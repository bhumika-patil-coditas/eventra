from fastapi import HTTPException, status

class CustomException:

    @staticmethod
    def NotFoundError(resource: str = "Resource", resource_id=None, message: str | None = None) -> HTTPException:
        detail = message or f"{resource} not found."
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    @staticmethod
    def InternalError(message: str = "Internal server error") -> HTTPException:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message)