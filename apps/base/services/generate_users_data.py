from faker import Faker

faker = Faker()


def generate_fake_name() -> str:
    return faker.first_name()
