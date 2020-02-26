import logging

from pydantic import BaseSettings

from .__version__ import __version__

logging.basicConfig(
    datefmt="%F %T", format="[%(asctime)s] %(levelname)s:%(module)s:%(lineno)d: %(message)s", level=logging.DEBUG,
)


class EnvironmentSettings(BaseSettings):
    SENTRY_SDK_DSN: str  # https://docs.sentry.io/error-reporting/quickstart/?platform=python#configure-the-sdk


environment_settings = EnvironmentSettings()


PROJECT_NAME = "hello-sentry"
RELEASE = f"{PROJECT_NAME}@{__version__}"
