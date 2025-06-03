class User:
    __slots__ = ('username', 'password', 'is_active')
    def __init__(self, username: str = None, password: str = None, is_active: bool = None):
        self.username = username
        self.password = password
        self.is_active = is_active

    def __repr__(self):
        return f'<User username="{self.username}" password="{self.password}" is_active="{self.is_active}">'