from django.core.management import BaseCommand, CommandParser

from apps.superuser_hw.models import Request


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--anonymous-only", action="store_true", help="Delete requests from anonymous users", default=False
        )

    def handle(self, *args, **options):
        if options.get("anonymous_only"):
            Request.objects.filter(user_id=None).delete()
            self.stdout.write("Requests from anonymous users deleted")
            return
        Request.objects.all().delete()
        self.stdout.write("All records deleted")
