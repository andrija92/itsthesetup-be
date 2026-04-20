# management/commands/seed.py
from django.core.management.base import BaseCommand
from api.factory.factories import UserFactory, SetupFactory

class Command(BaseCommand):
    help = 'Seed users only'

    def add_arguments(self, parser):
        parser.add_argument('--batch', type=int, default=10)

    def handle(self, *args, **options):
        UserFactory.create_batch(options['batch'])
        self.stdout.write(self.style.SUCCESS('Done!'))