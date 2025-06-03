from src.database.connector import PGConnector


class InitializeDatabaseInteractor:
    def __init__(self, connector: PGConnector):
        self.connector = connector

    async def _create_tables(self) -> None:
        table_create_queries: list[str] = ['''CREATE TABLE IF NOT EXISTS users (
                                              id SERIAL PRIMARY KEY,
                                              username TEXT UNIQUE NOT NULL,
                                              password TEXT NOT NULL)'''
                                           ]
        async with self.connector as connection:
            for table_create_query in table_create_queries:
                await connection.execute(table_create_query)

        return

    async def _create_database(self) -> None:
        query = """SELECT FROM pg_database WHERE datname = 'echoapi'"""
        async with self.connector as conn:
            is_exists = await conn.execute(query)

        if is_exists == 'SELECT 0':
            query: str = '''CREATE DATABASE echoapi'''
            async with self.connector as conn:
                await conn.execute(query)
        self.connector.change_database('echoapi')
        return

    async def __call__(self) -> None:
        await self._create_database()
        await self._create_tables()

