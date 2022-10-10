from django.core.management import BaseCommand
from apps.contacts import models
from apps.contacts.services import generate_fake_contacts


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        amount_contacts = options["amount_contacts"]
        contacts = generate_fake_contacts()
