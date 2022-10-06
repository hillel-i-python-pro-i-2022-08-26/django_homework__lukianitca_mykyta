from typing import NamedTuple


class User(NamedTuple):
    username: str
    email: str
    password: str

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        return self.username == other.username
