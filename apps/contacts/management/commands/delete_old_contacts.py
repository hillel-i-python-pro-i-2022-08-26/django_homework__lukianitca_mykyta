import logging

from django.core.management import BaseCommand
from django.utils import timezone

from apps.contacts.models import Contacts


class Command(BaseCommand):
    help = "Delete old data from contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def handle(self, *args, **options):
        datetime_delete = timezone.now() - timezone.timedelta(minutes=1)
        sorted_contacts = Contacts.objects.order_by("created_at").filter(created_at__lt=datetime_delete)
        if not sorted_contacts:
            self.logger.info("Old data was not found")
            return
        self.logger.info("Start deleting old contacts")
        sorted_contacts.delete()
        self.logger.info("Old data deleted")
