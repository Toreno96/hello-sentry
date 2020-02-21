import logging
import os

import sentry_sdk

SENTRY_SDK_DSN = os.getenv("SENTRY_SDK_DSN")

logging.basicConfig(
    datefmt="%F %T",
    format="[%(asctime)s] %(levelname)s:%(module)s:%(lineno)d: %(message)s",
    level=logging.DEBUG,
)

sentry_sdk.init(SENTRY_SDK_DSN)


def main():
    division_by_zero = 1 / 0
    print(division_by_zero)


if __name__ == "__main__":
    main()
