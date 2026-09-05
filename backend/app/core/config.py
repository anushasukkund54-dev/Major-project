from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "AI Job Search & Resume Matcher"
    APP_VERSION: str = "1.0.0"

    # Adzuna Job Search API
    ADZUNA_APP_ID: str
    ADZUNA_APP_KEY: str

    # Ollama / Local LLM
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()