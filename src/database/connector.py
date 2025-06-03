import asyncpg
from asyncpg import Connection


class PGConnector:
    _kwargs = None
    _instance = None

    def __new__(cls,
                user: str,
                password: str,
                host: str = 'localhost',
                port: int = 5432,
                database: str | None = 'echoapi'):
        if cls._instance is None:
            cls._kwargs = {'user': user,
                           'password': password,
                           'host': host,
                           'port': port}
            if database:
                cls._kwargs['database'] = database

            cls._instance = super(PGConnector, cls).__new__(cls)

        return cls._instance

    async def __aenter__(self) -> Connection:
        self.connection = await asyncpg.connect(**PGConnector._kwargs)
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection.close()

    @classmethod
    def change_database(cls, database: str = 'echoapi'):
        cls._kwargs['database'] = database
