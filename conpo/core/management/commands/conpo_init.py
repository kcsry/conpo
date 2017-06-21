from random import randint

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

from conpo.core.models import Event
from conpo.testing.data import create_competition


def generate_gibberish():
    return get_random_string(randint(5, 15), 'pipapo mimamo riraro').strip().title()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--demo', action='store_true', default=False)

    def handle(self, demo, **options):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            self.stdout.write('Creating superuser: admin / admin')
            User.objects.create_superuser(username='admin', password='admin', email='admin@example.com')
        if demo:
            self.create_demo_data()

    def create_demo_data(self):
        event = Event.objects.first()
        if not event:
            self.stdout.write('Creating demo event')
            event = Event.objects.create(name='Demo Event', slug='demo-event', published=True)
        self.stdout.write('Using event: %s' % event)
        while event.competitions.count() < 5:
            compo = create_competition(event)
            self.stdout.write('Created %s' % compo)
