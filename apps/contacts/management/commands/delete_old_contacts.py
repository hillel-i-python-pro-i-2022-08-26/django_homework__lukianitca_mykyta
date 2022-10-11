import logging

from django.core.management import BaseCommand, CommandParser
from django.utils import timezone

from apps.contacts.models import Contacts


class Command(BaseCommand):
    help = "Delete old data from contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def handle(self, *args, **options):
        self.logger.info("Start deleting old contacts")
        sorted_contacts = Contacts.objects.order_by("created_at")
        datetime_delete = timezone.now() - timezone.timedelta(minutes=1)
        sorted_contacts.filter(created_at__lt=datetime_delete).delete()
        self.logger.info("Old data deleted")

