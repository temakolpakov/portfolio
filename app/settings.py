import logging
import os
import sys

from configs_validator import ConfigsValidator
from dotenv import load_dotenv
from logging_utils.colors_formatter import ColorFormatter
from pydantic import ValidationError

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
root_logger = logging.getLogger()
root_logger.removeHandler(*root_logger.handlers)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(ColorFormatter())
root_logger.addHandler(consoleHandler)

_logger = logging.getLogger(__name__)

# This flag available only in production enviroment
is_prod = os.environ.get('IS_PROD') in [1, True, 'true', 'True']

if is_prod:
    root_logger.setLevel(logging.INFO)
else:
    root_logger.setLevel(logging.DEBUG)
    load_dotenv(dotenv_path='/Users/artemkolpakov/PycharmProjects/portfolio/app/configs/.env')
    load_dotenv(dotenv_path=os.path.join('configs', '.env'))
    load_dotenv(dotenv_path=os.path.join('.', 'configs','.env'))


try:
    config_parameters = ConfigsValidator(**os.environ)
except ValidationError as e:
    _logger.critical(exc_info=e, msg='Env parameters validation')
    sys.exit(-1)

config_parameters.IS_PROD = is_prod

config_parameters.API_URL = f'http://{config_parameters.API_HOST}:{config_parameters.API_PORT}'
#
# config_parameters.REDIS_URL = f'redis://:{config_parameters.REDIS_PASSWORD}@{config_parameters.REDIS_HOST}:{config_parameters.REDIS_PORT}/{config_parameters.REDIS_DB}'

config_parameters.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

