import tomllib


class GetConfig:
    @staticmethod
    def get_database_config() -> dict:
        with open("secret_data/config.toml", "rb") as config:
            config = tomllib.load(config)["Database"]

        return config
