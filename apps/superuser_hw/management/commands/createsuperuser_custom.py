from django.core.management import BaseCommand, CommandParser
from django.db import IntegrityError

from apps.superuser_hw.models import User


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser):
        parser.add_argument("--username", default="admin", type=str, help="Admin username")
        parser.add_argument("--email", default="admin@mail.com", type=str, help="Admin email")
        parser.add_argument("--password", default="admin123", type=str, help="Admin password")

    def handle(self, *args, **options):
        admin_data = {
            "username": options["username"],
            "email": options["email"],
            "password": options["password"],
        }
        try:
            admin = User.objects.create_superuser(**admin_data)
            print(f"Admin info for login: {admin_data}")
        except IntegrityError:
            print("User already exists")
