from src.database.connector import PGConnector
from src.database.dto.users_dto import UsersDTO


class UsersDAO:
    def __init__(self, connector: PGConnector):
        self.connector = connector

    async def create_user(self, username: str, password: str, is_active: bool = False):
        async with self.connector as connection:
            await connection.execute('''INSERT INTO users (username, password, is_active) VALUES ($1, $2, $3) ON CONFLICT (username) DO NOTHING''', username, password, is_active)

    async def get_user(self, username: str):
        async with self.connector as connection:
            user = await connection.fetchrow('''SELECT * FROM users WHERE username = $1''', username)
        return UsersDTO.get_user(user)

    async def change_user_activity(self, username: str, is_active: bool):
        async with self.connector as connection:
            await connection.execute('''UPDATE users SET is_active = $1 WHERE username = $2''', is_active, username)

