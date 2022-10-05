from faker import Faker
from apps.base.services.models import User
from uuid import uuid4, UUID
from faker.exceptions import UniquenessException
from apps.base.services import get_safe_chars
from random import choice, randint
from itertools import chain
from sys import getsizeof


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


# class UsersDataGenerator:
#     def __init__(self, amount_users: int):
#         self.amount_users: int = amount_users
#         self._unique_usernames: set = set()
#         self.faker = FakeEngine()
#         self.username_function = self.faker.standard_fake_username
#
#     def generate_fake_user(self):
#         fake_name = self.username_function()
#         return {
#             "username": fake_name,
#             "email": self.faker.generate_fake_email(fake_name),
#             "password": self.faker.generate_fake_password(),
#         }

# def get_fake_user(self):
#     try:


# def generate_users_faker(self):
#     while len(self._unique_usernames) < self.amount_users:
#         fake_username = self.faker.standard_fake_username()
#         self._unique_usernames.add(fake_username)
#         user_data = self.generate_fake_user(fake_username)
#         yield User(**user_data)
#
# def generate_users_ascii(self):
#     safe_chars = get_safe_chars()
#     while len(self._unique_usernames) < self.amount_users:
#         fake_username = self.emergency_username_generation(safe_chars)
#         self._unique_usernames.add(fake_username)
#         user_data = self.generate_fake_user(fake_username)
#         yield User(**user_data)

# @staticmethod
# def emergency_username_generation(allowed_chars):
#     return "".join(choice(allowed_chars) for _ in range(randint(8, 18)))


# def get_fake_users(self):
# try:
#     return self.generate_users_faker()
# except UniquenessException:
#     return self.generate_users_ascii()


# def generate_fake_name() -> str:
#     return faker.first_name()
#
#
# def generate_fake_username():
#     return faker.unique.user_name()
#
#
# def generate_fake_password() -> UUID:
#     return uuid4()
#
#
# def generate_fake_email(base_name: str) -> str:
#     base_fake_email: list = faker.email().split("@")
#     base_fake_email[0] = base_name
#     return "@".join(base_fake_email)
#
#
# def standard_fake_username():
#     return faker.unique.user_name()
#
#
# def emergency_username_generation(allowed_chars):
#     return "".join(choice(allowed_chars) for _ in range(randint(8, 18)))
#
#
# def generate_fake_default(base_name) -> dict:
#     return {
#         "username": base_name,
#         "email": generate_fake_email(base_name),
#         "password": generate_fake_password(),
#     }


# def get_fake_users(amount_users: int):
#     unique_usernames: set = set()
#     try:
#         while len(_unique_usernames) < amount_users:
#             fake_username = standard_fake_username()
#             unique_usernames.add(fake_username)
#             user_data = generate_fake_default(fake_username)
#             yield User(**user_data)
#     except UniquenessException:
#         safe_chars = get_safe_chars()
#         while len(_unique_usernames) < amount_users:
#             fake_username = emergency_username_generation(safe_chars)
#             unique_usernames.add(fake_username)
#             user_data = generate_fake_default(fake_username)
#             yield User(**user_data)


# def get_fake_users(amount_users: int):
#     while


class UsersDataGenerator:
    def __init__(self, amount_users: int):
        self.amount_users = amount_users
        self._unique_users = set()
        self._faker = FakeEngine()
        self._username_function = self._faker.standard_fake_username
        self._allowed_chars = get_safe_chars()

    def generate_one_user(self) -> dict:
        fake_username = self._username_function()
        return {
            "username": fake_username,
            "email": self._faker.generate_fake_email(fake_username),
            "password": self._faker.generate_fake_password(),
        }

    def emergency_username_generation(self):
        return "".join(choice(self._allowed_chars) for _ in range(randint(8, 18)))

    def generate_users(self):
        try:
            while len(self._unique_users) < self.amount_users:
                fake_user_data = self.generate_one_user()
                fake_user_object = User(**fake_user_data)
                self._unique_users.add(fake_user_object)
        except UniquenessException:
            self._username_function = self.emergency_username_generation
            self.generate_users()

    @property
    def unique_users(self):
        self.generate_users()
        return list(self._unique_users)


# if __name__ == "__main__":
#     # gen = UsersDataGenerator(30).get_fake_users()
#     # for el in gen:
#     #     print(el)
#     fake = UsersDataGenerator(2).faker
#     s1 = set()
#     # l1 = []
#     for _ in range(100000):
#         un = fake.standard_fake_username()
#         s1.add(User(un, fake.generate_fake_email(un), str(fake.generate_fake_password())))
#     print(getsizeof(s1))
#     # for _ in range(100000):
#     #     un = fake.standard_fake_username()
#     #     l1.append(User(un, fake.generate_fake_email(un), str(fake.generate_fake_password())))
#
#     # print(getsizeof(s1))
#     l1 = list(s1)
#     print(getsizeof(l1))
#     # for el in chain.from_iterable((s1, s2)):
#     #     print(el)


if __name__ == "__main__":
    users_gen = UsersDataGenerator(100_000)
    list_users = users_gen.unique_users
    print(getsizeof(list_users))
