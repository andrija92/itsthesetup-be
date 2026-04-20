# management/commands/seed.py
from django.core.management.base import BaseCommand
from api.factory.factories import CarFactory, UserFactory, SetupFactory, TrackFactory
from api.models import Game

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10)
        parser.add_argument('--setups', type=int, default=20)
        parser.add_argument('--tracks', type=int, default=20)
        parser.add_argument('--cars', type=int, default=20)

    def handle(self, *args, **options):
        games = list(Game.objects.all()[:3])
        self.stdout.write('Seeding tracks...')
        TrackFactory.create_batch(options['tracks'], games=games)
        self.stdout.write('Seeding cars...')
        CarFactory.create_batch(options['cars'], games=games)
        self.stdout.write('Seeding setups...')
        SetupFactory.create_batch(options['setups'])
        self.stdout.write(self.style.SUCCESS('Done!'))