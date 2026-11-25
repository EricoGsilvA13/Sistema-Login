from pathlib import Path
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PASTA_BACKEND = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PASTA_BACKEND / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    db_host: str
    db_port: int = 3306
    db_user: str
    db_password: SecretStr
    db_name: str


settings = Settings() # pyright: ignore[reportCallIssue]