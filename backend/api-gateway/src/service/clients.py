import json
from src.constants import ServiceEnum
import requests
from fastapi import HTTPException, status

class Clients:

    def __init__(self, service:str, base_url:str, endpoints:dict[str, str]):
        self.service = ServiceEnum(service)
        self.base_url = base_url
        self.endpoints = endpoints


    def call(self, request, payload:dict):
        if request in self.endpoints:
            method, endpoint = self.endpoints[request].split(" ", 1)

            if method == "GET":
                response =requests.get(url=f"{self.base_url}{endpoint}", params=payload)
            elif method == "POST":
                response = requests.post(url=f"{self.base_url}{endpoint}", json=payload)
            elif method == "PATCH":
                response = requests.patch(url=f"{self.base_url}{endpoint}", json=payload)
            elif method == "DELETE":
                response = requests.delete(url=f"{self.base_url}{endpoint}", json=payload)
            else:
                raise HTTPException(status_code=500)
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=json.loads(response.content))
            elif response.status_code == 200:
                return json.loads(response.content)
            else:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)  
    
            




    