from src.database.connector import PGConnector
from src.database.dto.users_dto import UsersDTO


class UsersDAO:
    def __init__(self, connector: PGConnector):
        self.connector = connector

    async def create_user(self, username: str, password: str):
        async with self.connector as connection:
            await connection.execute('''INSERT INTO users (username, password) VALUES ($1, $2) ON CONFLICT (username) DO NOTHING''', username, password)

    async def get_user(self, username: str):
        async with self.connector as connection:
            user = await connection.fetchrow('''SELECT * FROM users WHERE username = $1''', username)
        return UsersDTO.get_user(user)

