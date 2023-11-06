from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    POSTGRES_CONTAINER_NAME: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    POSTGRES_URL_IN_DOCKER: str = f'postgresql+asyncpg://postgres:postgres@postgres:5432/foo'
    POSTGRE_URL_OUT_DOCKER: str = f'postgresql+asyncpg://postgres:postgres@localhost:5432/foo'
    APP_HOST: str
    APP_PORT: int
