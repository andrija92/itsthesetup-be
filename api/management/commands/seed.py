# management/commands/seed.py
from django.core.management.base import BaseCommand
from api.factory.factories import UserFactory, SetupFactory

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10)
        parser.add_argument('--setups', type=int, default=20)

    def handle(self, *args, **options):
        self.stdout.write('Seeding...')
        self.stdout.write('Seeding users...')
        UserFactory.create_batch(options['users'])
        self.stdout.write('Seeding setups...')
        SetupFactory.create_batch(options['setups'])
        self.stdout.write(self.style.SUCCESS('Done!'))