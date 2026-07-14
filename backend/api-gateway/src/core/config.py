from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    LOG_LEVEL: str
    LOG_FILE:str

    PUBLIC_KEY_FILEPATH:str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

SETTINGS = Config()