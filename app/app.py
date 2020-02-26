import sentry_sdk

import __metadata__
import settings

sentry_sdk.init(settings.environment_settings.SENTRY_SDK_DSN, release=__metadata__.__release__)


def main():
    count = 10
    lst = list(range(count))
    print(lst[count - 1])
    raise ArithmeticError


if __name__ == "__main__":
    main()
