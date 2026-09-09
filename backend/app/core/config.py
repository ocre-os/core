from functools import lru_cache

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(
        default="Ocre OS API",
        validation_alias=AliasChoices("OCRE_APP_NAME", "APP_NAME"),
    )
    env: str = Field(
        default="development",
        validation_alias=AliasChoices("OCRE_ENV", "ENV"),
    )
    database_url: str = Field(
        default="postgresql+psycopg://ocre_os:change_me@db:5432/ocre_os",
        validation_alias=AliasChoices("DATABASE_URL", "OCRE_DATABASE_URL"),
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
