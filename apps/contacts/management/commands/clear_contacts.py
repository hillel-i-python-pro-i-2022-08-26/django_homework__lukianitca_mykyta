import logging

from django.core.management import BaseCommand, CommandParser
from apps.contacts.models import Contacts


class Command(BaseCommand):
    help = "Clear all contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def handle(self, *args, **options):
        self.logger.info("Start clear contacts")
        Contacts.objects.all().delete()
        self.logger.info("Contacts cleared")

