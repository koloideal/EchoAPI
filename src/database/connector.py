import asyncpg
from asyncpg import Connection


class PGConnector:
    _kwargs = None
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            cls._kwargs = kwargs
            cls._instance = super(PGConnector, cls).__new__(cls)

        return cls._instance

    async def __aenter__(self) -> Connection:
        self.connection = await asyncpg.connect(**PGConnector._kwargs)
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection.close()

    @classmethod
    def __del__(cls):
        if cls._instance:
            del cls


