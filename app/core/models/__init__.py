from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from settings import config_parameters

tortoise_credentials = {
    "host": config_parameters.POSTGRES_DB_HOST,
    "port": config_parameters.POSTGRES_DB_PORT,
    "user": config_parameters.POSTGRES_DB_USERNAME,
    "password": config_parameters.POSTGRES_DB_PASSWORD,
    "database": config_parameters.POSTGRES_DB_NAME,
}
tortoise_connection_config = {
    'connections': {
        'default': {
            "engine": "tortoise.backends.asyncpg",
            "credentials": tortoise_credentials,
            'max_size': 1000,
        }
    },
    "apps": {
        "models": {
            "models": [
                "core.models.models",
                "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}


def init(server: FastAPI):
    register_tortoise(
        server,
        config=tortoise_connection_config,
        generate_schemas=True
    )
