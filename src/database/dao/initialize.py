from src.database.connector import PGConnector


class InitializeDatabaseInteractor:
    def __init__(self, connector: PGConnector):
        self.connector = connector

    async def create_tables(self) -> None:
        table_create_queries: list[str] = ["""CREATE TABLE IF NOT EXISTS users (
                                              id SERIAL PRIMARY KEY,
                                              username TEXT NOT NULL,
                                              password TEXT NOT NULL"""
                                           ]
        async with self.connector as connection:
            for table_create_query in table_create_queries:
                await connection.execute(table_create_query)

        return

    async def create_database(self) -> None:
        query = """DO
                   $$
                   BEGIN
                      IF NOT EXISTS (
                         SELECT FROM pg_database WHERE datname = 'echoapi'
                      ) THEN
                         CREATE DATABASE echoapi;
                      END IF;
                   END
                   $$;"""
        async with self.connector as connection:
            await connection.execute(query)

        del PGConnector
        return

    def __call__(self, username: str, password: str, host: str, port: int) -> None:
        self.username = username
        self.password = password

