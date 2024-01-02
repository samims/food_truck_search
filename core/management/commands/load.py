import logging

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from .csv_file_read import read_data

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "load initial data"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        """
        Seed data from the csv file
        """
        try:
            read_data()
        except IntegrityError as e:
            logger.error("data already populated")
