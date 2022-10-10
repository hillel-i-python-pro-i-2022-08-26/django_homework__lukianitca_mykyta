from faker import Faker
from typing import Iterator
from apps.contacts.services import T_CONTACT

from apps.contacts.services import Contact


class FakeProvide:
    def __init__(self):
        self._faker = Faker()

    def generate_one_contact(self, minimal_age: int = 11) -> T_CONTACT:
        fake_user_data = {
            "contact_name": self._faker.fake_name(),
            "phone_number": self._faker.phone_number(),
            "birth_date": self._faker.date_of_birth(minimum_age=minimal_age),
        }
        return Contact(**fake_user_data)


def generate_fake_contacts(amount_contacts: int = 10) -> Iterator[T_CONTACT]:
    faker = FakeProvide()
    for _ in range(amount_contacts):
        yield faker.generate_one_contact()
