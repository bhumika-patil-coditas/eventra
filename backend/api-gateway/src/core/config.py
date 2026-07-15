from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    LOG_LEVEL: str
    LOG_FILE:str

    PUBLIC_KEY_FILEPATH:str
    PRIVATE_KEY_FOR_HS: str

    REDIS_URL: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

SETTINGS = Config()