from faker import Faker
from apps.base.services.models import User
from uuid import uuid4, UUID
from faker.exceptions import UniquenessException
from apps.base.services import get_safe_chars
from random import choice, randint


class FakeEngine:
    def __init__(self):
        self._faker = Faker()

    def generate_fake_name(self) -> str:
        return self._faker.first_name()

    def generate_fake_password(self) -> UUID:
        return self._faker.password()

    def standard_fake_username(self):
        return self._faker.unique.user_name()

    def generate_fake_email(self, base_name: str) -> str:
        base_fake_email: list = self._faker.email().split("@")
        base_fake_email[0] = base_name
        return "@".join(base_fake_email)


class UsersDataGenerator:
    def __init__(self):
        self._unique_username: set = {}
        self._faker = FakeEngine()

    def generate_fake_user(self, base_name: str):
        return {
            "username": base_name,
            "email": generate_fake_email(base_name),
            "password": generate_fake_password(),
        }


def generate_fake_name() -> str:
    return faker.first_name()


def generate_fake_username():
    return faker.unique.user_name()


def generate_fake_password() -> UUID:
    return uuid4()


def generate_fake_email(base_name: str) -> str:
    base_fake_email: list = faker.email().split("@")
    base_fake_email[0] = base_name
    return "@".join(base_fake_email)


def standard_fake_username():
    return faker.unique.user_name()


def emergency_username_generation(allowed_chars):
    return "".join(choice(allowed_chars) for _ in range(randint(8, 18)))


def generate_fake_default(base_name) -> dict:
    return {
        "username": base_name,
        "email": generate_fake_email(base_name),
        "password": generate_fake_password(),
    }


def get_fake_users(amount_users: int):
    unique_usernames: set = set()
    try:
        while len(unique_usernames) < amount_users:
            fake_username = standard_fake_username()
            unique_usernames.add(fake_username)
            user_data = generate_fake_default(fake_username)
            yield User(**user_data)
    except UniquenessException:
        safe_chars = get_safe_chars()
        while len(unique_usernames) < amount_users:
            fake_username = emergency_username_generation(safe_chars)
            unique_usernames.add(fake_username)
            user_data = generate_fake_default(fake_username)
            yield User(**user_data)


if __name__ == "__main__":
    f = get_fake_users(100000)
    l = list(f)
    print(l[-1])
    print(len(set(l)))
