from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Ocre OS API"
    env: str = "development"
    database_url: str = "postgresql+psycopg://ocre_os:change_me@db:5432/ocre_os"

    model_config = SettingsConfigDict(
        env_prefix="OCRE_",
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
