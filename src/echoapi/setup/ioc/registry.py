from collections.abc import Iterable

from dishka import Provider
from dishka.integrations.fastapi import FastapiProvider

from echoapi.setup.ioc.providers import ConfigProvider


def get_providers() -> Iterable[Provider]:
    return (
        ConfigProvider(),
        FastapiProvider()
    )