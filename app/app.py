import sentry_sdk

import settings

sentry_sdk.init(settings.environment_settings.SENTRY_SDK_DSN, release=settings.RELEASE)


def main():
    count = 10
    lst = list(range(count))
    print(lst[count - 1])
    print(1 / 0)


if __name__ == "__main__":
    main()
