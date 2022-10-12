import logging

from django.core.management import BaseCommand

from apps.contacts.models import Contacts


class Command(BaseCommand):
    help = "Clear all contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def handle(self, *args, **options):
        old_contacts = Contacts.objects.all()
        if not old_contacts:
            self.logger.info("Contact's list already empty")
            return
        self.logger.info("Start clear contacts")
        old_contacts.delete()
        self.logger.info("Contacts cleared")
