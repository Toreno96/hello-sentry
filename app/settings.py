import logging
import os

SENTRY_SDK_DSN = os.getenv("SENTRY_SDK_DSN")

logging.basicConfig(
    datefmt="%F %T",
    format="[%(asctime)s] %(levelname)s:%(module)s:%(lineno)d: %(message)s",
    level=logging.DEBUG,
)
