from pydantic_settings import BaseSettings

class Settings(BaseSettings):
PROJECT_NAME: str = "InfraSyntax"
ES_HOST: str
ES_PORT: int
ES_INDEX: str
MODEL_NAME: str
EMBEDDING_DIMS: int

class Config:
    env_file = ".env"
settings = Settings()
