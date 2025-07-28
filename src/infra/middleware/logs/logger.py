import logging
import os

import ecs_logging

job_log_level = os.getenv("JOB_LOG_LEVEL", "INFO")

handler = logging.StreamHandler()
handler.setFormatter(ecs_logging.StdlibFormatter())

logger = logging.getLogger("logger")
logger.setLevel(getattr(logging, job_log_level.upper(), logging.INFO))
logger.addHandler(handler)
logger.propagate = False


def debug(message):
    def handle_debug(func):
        def inner_function(*args, **kwargs):
            logger.debug(f"{message}")
            return func(*args, **kwargs)

        return inner_function

    return handle_debug


def info(message):
    def handle_info(func):
        def inner_function(*args, **kwargs):
            logger.info(f"{message}")
            return func(*args, **kwargs)

        return inner_function

    return handle_info
