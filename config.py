from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    tapis_base_url: str
    param_server_url: str = ""  # unused by this service
    mongodb_uri: str
    class Config:
        env_file: str = ".env"
        extra = "ignore"

app_settings = AppSettings()