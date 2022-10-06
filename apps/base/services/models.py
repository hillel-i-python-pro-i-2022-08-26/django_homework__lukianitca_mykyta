from typing import NamedTuple

from apps.base.services.fake_data_types import T_PASSWORD, T_USERNAME, T_EMAIL


class User(NamedTuple):
    username: T_USERNAME
    email: T_EMAIL
    password: T_PASSWORD

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        return self.username == other.username
