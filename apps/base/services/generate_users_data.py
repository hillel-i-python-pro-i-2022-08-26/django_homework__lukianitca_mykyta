from apps.base.services import faker
from apps.base.services.models import User
from uuid import uuid4, UUID
from faker.exceptions import UniquenessException
from .get_additional_data import get_safe_chars


def generate_fake_name() -> str:
    return faker.first_name()


def generate_fake_username():
    return faker.unique.user_name()


def generate_fake_password() -> UUID:
    return uuid4()


def generate_fake_email(base_name: str) -> str:
    base_fake_email: list = faker.email().split("@")
    base_fake_email[0] = base_name
    return "".join(base_fake_email)


def standard_fake_username():
    return faker.unique.user_name()


def emergency_username_generation():
    return


def get_fake_users(amount_users: int):
    unique_usernames: set = set()
    try:
        while len(unique_usernames) < amount_users:
            fake_username = standard_fake_username()
            unique_usernames.add(fake_username)
            fake_email = generate_fake_email(fake_username)
            fake_password = generate_fake_password()
            yield User(fake_username, fake_email, str(fake_password))
    except UniquenessException:
        users_deficit = amount_users - len(unique_usernames)
        for _ in range(users_deficit):
            fake_username = emergency_username_generation()
            fake_email = generate_fake_email(fake_username)
            fake_password = generate_fake_password()
            yield User(fake_username, fake_email, str(fake_password))


# if __name__ == '__main__':
# print(list(string.ascii_lowercase+string.ascii_uppercase+string.digits+"_"))
