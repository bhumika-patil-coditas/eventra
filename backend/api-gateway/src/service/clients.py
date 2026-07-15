import requests
from fastapi import HTTPException, status
from src.constants import ServiceEnum

class Clients:
    def __init__(self, service: str, base_url: str, endpoints: dict[str, str]):
        self.service = ServiceEnum(service)
        self.base_url = base_url
        self.endpoints = endpoints

    def call(self, request: str, payload: dict):
        if request not in self.endpoints:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Unknown endpoint: {request}"
            )

        method, endpoint = self.endpoints[request].split(" ", 1)

        try:
            response = requests.request(
                method=method,
                url=f"{self.base_url}{endpoint}",
                params=payload if method == "GET" else None,
                json=payload if method != "GET" else None,
                timeout=10,
            )
        except requests.RequestException:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"{self.service.value} service unavailable"
            )

        if not response.ok:
            try:
                detail = response.json()
            except ValueError:
                detail = response.text

            raise HTTPException(
                status_code=response.status_code,
                detail=detail
            )

        if response.status_code == 204:
            return None

        try:
            return response.json()
        except ValueError:
            return response.text