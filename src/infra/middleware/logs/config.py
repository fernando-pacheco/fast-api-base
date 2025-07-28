import sys
from logging.config import dictConfig


class Logging:
    def configure(self):
        logging_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s [%(levelname)s] [%(name)s]: %(message)s",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": sys.stdout,
                },
            },
            "root": {
                "level": "DEBUG",
                "handlers": ["console"],
            },
        }

        dictConfig(logging_config)
