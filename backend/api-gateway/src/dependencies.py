import json

from src.constants import ServiceEnum
from src.core import CustomException
from src.service.clients import Clients


class Microservice:
    _services: dict[ServiceEnum, Clients] | None = None

    @classmethod
    def get_service_dict(cls) -> dict[ServiceEnum, Clients]:
        if cls._services is not None:
            return cls._services

        with open("clients.json", "r") as f:
            config = json.load(f)

        cls._services = {
            ServiceEnum(name): Clients(
                service=name,
                base_url=data["base_url"],
                endpoints=data["endpoints"],
            )
            for name, data in config.items()
        }

        return cls._services

    @classmethod
    def get_service(cls, services: list[ServiceEnum]):
        all_services = cls.get_service_dict()

        missing = [service for service in services if service not in all_services]
        if missing:
            raise CustomException.ConflictError(
                resource="service-name",
                message=f"Service(s) unavailable: {', '.join(s.value for s in missing)}",
            )

        def return_service() -> dict[ServiceEnum, Clients]:
            return {
                service: all_services[service]
                for service in services
            }

        return return_service