from typing import Union

from pydantic import BaseModel


class MetaConfigsModel(BaseModel):
    IS_PROD: Union[bool] = True


class APIConfigsModel(BaseModel):
    API_HOST: Union[str]
    API_PORT: Union[int]
    API_URL: Union[str, None] = None
    BASE_DIR: Union[str, None] = None
    TEMPLATES_DIR: Union[str, None] = None
    # LOCALES_DIR: Union[str, None] = None
    # GUIDE_LINK: Union[str, None] = None
    # UPLOADED_FILES_DIR: Union[str, None] = None
    # BOT_LINK: Union[str]


class PostgresDataBaseConfigsModel(BaseModel):
    POSTGRES_DB_USERNAME: Union[str]
    POSTGRES_DB_PASSWORD: Union[str]
    POSTGRES_DB_HOST: Union[str]
    POSTGRES_DB_PORT: Union[int]
    POSTGRES_DB_NAME: Union[str]


# class RedisConfigsModel(BaseModel):
#     REDIS_HOST: Union[str]
#     REDIS_PORT: Union[int]
#     REDIS_PASSWORD: Union[str]
#     REDIS_DB: Union[int]
#     REDIS_URL: Union[str, None] = None


class ConfigsValidator(APIConfigsModel, PostgresDataBaseConfigsModel, MetaConfigsModel,
                       # RedisConfigsModel
                       ):
    pass
