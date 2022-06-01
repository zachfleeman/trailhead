from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, PostgresDsn, EmailStr, validator

class Settings(BaseSettings):
    API_STR: str = "/api"
    PROJECT_NAME: str = "trailhead"

settings = Settings()