from src.constants import ServiceEnum
from src.service.clients import Clients
import json
from src.core import CustomException

class Microservice:
    
    @classmethod
    def get_service_dict(cls):
        services_dict:dict[ServiceEnum, Clients] = {}

        with open("clients.json", "r") as f:
            data:dict[str, dict] = json.loads(f.read())

        for service, data in data.items():
            services_dict[ServiceEnum(service)] = Clients(service=service, base_url=data["base_url"], endpoints=data["endpoints"])
        
        return services_dict
    
    @classmethod
    def get_service(cls, services:list[ServiceEnum]):
        all_services = cls.get_service_dict()
        required_service = {}

        for serv in services:
            if serv not in all_services:
                raise CustomException.ConflictError(resource="service-name" , message="Service unavaliable")
            else:
                required_service[serv] = all_services[serv]

        def return_service() -> dict[ServiceEnum, Clients]:
            return required_service
        
        return return_service
