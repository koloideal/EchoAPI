from asyncpg import Record

from src.database.models import User


class UsersDTO:
    @staticmethod
    def get_user(user: Record | None) -> User | None:
        if user:
            return User(username=user['username'],
                        password=user['password'],
                        is_active=user['is_active'])
        else:
            return None
