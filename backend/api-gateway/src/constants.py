from enum import Enum

class ServiceEnum(Enum):

    AUTH = "auth"
    AWS = "aws"

class RolesEnum(Enum):

    ORGANISER = "organiser"
    VENDOR = "vendor"
    ADMIN = "admin"