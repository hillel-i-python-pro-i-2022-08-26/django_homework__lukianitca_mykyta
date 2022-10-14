import logging

from django.core.management import BaseCommand, CommandParser

from apps.contacts.models import Contact
from apps.contacts.services import generate_fake_contacts


class Command(BaseCommand):
    help = "Generate and save fake contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--amount",
            type=int,
            default=20,
            help="Amount of contacts to generate"
        )

    def handle(self, *args, **options):
        amount_contacts = options["amount"]
        if amount_contacts <= 0:
            self.logger.critical("Amount of contacts must be natural number!")
            return

        self.logger.info(f"Contacts to generate: {amount_contacts}")
        current_amount_contacts = Contact.objects.all().count()
        self.logger.info(f"Current amount of contacts: {current_amount_contacts}")
        for number, contact in enumerate(generate_fake_contacts(amount_contacts), start=1):
            contact.save()
            self.logger.info(f"Saved: {number}/{amount_contacts}")
        self.logger.info(f"{amount_contacts} contacts generated")
