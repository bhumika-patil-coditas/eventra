from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    AWS_ACCESS_KEY_ID :str
    AWS_SECRET_ACCESS_KEY :str
    AWS_REGION :str 
    S3_BUCKET_NAME :str

    LOG_LEVEL: str
    LOG_FILE:str

    ADMIN_MAIL:str


    model_config = SettingsConfigDict(
        env_file=".env"
    )

SETTINGS = Config()