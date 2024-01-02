from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "load initial data"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # TODO: will write here
        pass
