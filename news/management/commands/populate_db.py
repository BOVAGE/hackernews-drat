from django.core.management.base import BaseCommand
from news.utils import populate_100_items


class Command(BaseCommand):
    help = "Populate db with 100 items from hackernews"

    def handle(self, *args, **options):
        populate_100_items()
        self.stdout.write(self.style.SUCCESS("All 100 items Loaded Successfully"))
