from random import choice, randint

from faker import Faker
from faker.exceptions import UniquenessException

from apps.base.services import get_safe_chars
from apps.base.services.fake_data_types import *
from apps.base.services.models import User


class FakeEngine:
    def __init__(self):
        self._faker = Faker()

    def generate_fake_name(self) -> T_NAME:
        return self._faker.first_name()

    def generate_fake_password(self) -> T_PASSWORD:
        return self._faker.password()

    def standard_fake_username(self) -> T_USERNAME:
        return self._faker.unique.user_name()

    def generate_fake_email(self, base_name: T_USERNAME) -> T_EMAIL:
        base_fake_email: list = self._faker.email().split("@")
        base_fake_email[0] = base_name
        return "@".join(base_fake_email)


class UsersDataGenerator:
    def __init__(self, amount_users: int):
        self.amount_users = amount_users
        self._unique_users = set()
        self._faker = FakeEngine()
        self._username_function = self._faker.standard_fake_username
        self._allowed_chars = get_safe_chars()

    def generate_one_user(self) -> User:
        fake_username: T_USERNAME = self._username_function()
        user_data = {
            "username": fake_username,
            "email": self._faker.generate_fake_email(fake_username),
            "password": self._faker.generate_fake_password(),
        }
        return User(**user_data)

    def emergency_username_generation(self) -> T_USERNAME:
        return "".join(choice(self._allowed_chars) for _ in range(randint(8, 18)))

    def generate_users(self):
        try:
            while len(self._unique_users) < self.amount_users:
                fake_user = self.generate_one_user()
                self._unique_users.add(fake_user)
        except UniquenessException:
            self._username_function = self.emergency_username_generation
            self.generate_users()

    @property
    def unique_users(self):
        self.generate_users()
        return list(self._unique_users)
