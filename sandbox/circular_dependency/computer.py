from user import User


class Computer:
    def __init__(self, name, users=None):
        self.name = name
        self.users = users if users is not None else []

    def print_users(self):
        for user in self.users:
            print(user)


