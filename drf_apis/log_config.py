import errno
import os
from drf_apis.settings import BASE_DIR

LOG_DIR = str(BASE_DIR) + "/" + "/logs/"

try:
    os.makedirs(LOG_DIR)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

LOG_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'NOTSET',
        'handlers': ['error_file', 'info_file', 'console'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'stream': 'ext://sys.stdout',
        },
        'info_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'filename': LOG_DIR + 'info.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'error_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': LOG_DIR + 'errors.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 20,
        },
    },
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(module)-17s - %(name)s - line:%(lineno)-4d '
                      '%(levelname)-8s %(message)s',
        }
    }
}
