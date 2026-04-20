# api/management/commands/clear.py
from django.core.management.base import BaseCommand
from api.models import Setup, Game, Track, Car

class Command(BaseCommand):
    help = 'Clear all data from the database'

    def handle(self, *args, **options):
        self.stdout.write('Clearing setups...')
        Setup.objects.all().delete()
        self.stdout.write('Clearing tracks...')
        Track.objects.all().delete()
        self.stdout.write('Clearing cars...')
        Car.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Database cleared!'))