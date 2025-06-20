import tomllib
from dishka import Provider, provide, Scope


class ConfigProvider(Provider):
    @provide(scope=Scope.APP)
    def get_database_config(self) -> dict:
        with open("secret_data/config.toml", "rb") as config:
            config = tomllib.load(config)["Database"]

        return config
