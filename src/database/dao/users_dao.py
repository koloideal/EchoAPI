from src.database.connector import PGConnector


class UsersDAO:
    def __init__(self, connector: PGConnector):
        self.connector = connector

    async def create_user(self, user: str, password: str):
        async with self.connector as connection:
            await connection.execute('''INSERT INTO users (user, password) VALUES ($1, $2)''', user, password)

