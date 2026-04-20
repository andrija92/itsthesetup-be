# api/management/commands/clear.py
from django.core.management.base import BaseCommand
from api.models import User, Setup, Game, Track, Car

class Command(BaseCommand):
    help = 'Clear all data from the database'
    
    def handle(self, *args, **options):
        self.stdout.write('Clearing users only...')
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Users cleared!'))
