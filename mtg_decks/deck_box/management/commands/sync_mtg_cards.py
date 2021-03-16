from deck_box.services.card_sync.service import CardSyncService

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    # python manage.py audit_households_over_charge
    help = 'Add a card to the users collection'

    def add_arguments(self, parser):
        parser.add_argument('sync_type', type=str, nargs='?', default='set')

    def handle(self, *args, **options):
        card_sync = CardSyncService()
        if options['sync_type'] == 'card':
            card_sync.sync_cards()
        if options['sync_type'] == 'set':
            card_sync.sync_sets()
