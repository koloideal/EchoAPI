class User:
    __slots__ = ('username', 'password')
    def __init__(self, username: str = None, password: str = None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User username="{self.username}" password="{self.password}">'