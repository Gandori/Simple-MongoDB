from pydantic import Field
from pydantic_settings import BaseSettings


class MongoDBClientSettings(BaseSettings):
    host: str = Field(default='localhost', alias='MONGODB_HOST')
    port: int = Field(default=27017, alias='MONGODB_PORT')
    username: str = Field(default='user', alias='MONGODB_USERNAME')
    password: str = Field(default='user', alias='MONGODB_PASSWORD')
    db: str = Field(default='example', alias='MONGODB_DB')
    response_timeout: int = Field(default=5000, alias='MONGODB_RESPONSE_TIMEOUT')
    connection_timeout: int = Field(default=5000, alias='MONGODB_CONNECTION_TIMEOUT')

    @property
    def url(self) -> str:
        return f'mongodb://{self.username}:{self.password}@{self.host}:{self.port}'
