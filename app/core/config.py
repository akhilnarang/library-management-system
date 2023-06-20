from typing import Any

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    # Our PyMySQL DB URI
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int = 5432
    DB_SSLMODE: str = "disable"
    DB_URI: str = ""

    @validator("DB_URI", pre=True)
    def assemble_db_connection(cls, v: str, values: dict[str, Any]) -> str:
        if isinstance(v, str) and v:
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DB_USER"),
            password=values.get("DB_PASSWORD"),
            host=values.get("DB_HOST"),
            path=f"/{values.get('DB_NAME') or ''}",
            port=str(values.get("DB_PORT") or 5432),
        )

    APP_NAME = "Library Management System"

    class Config:
        env_file = ".env"


settings = Settings()
