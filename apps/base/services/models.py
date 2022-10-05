from typing import NamedTuple


class User(NamedTuple):
    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email
    #     self.password = password

    username: str
    email: str
    password: str

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        return self.username == other.username
