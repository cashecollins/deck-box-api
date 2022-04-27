import threading
import time
from mtgsdk import Card as api_cards
from mtgsdk import Set as api_set
from deck_box.models import Card, Set


class CardSyncService:
    def __init__(self):
        pass

    def sync_sets(self):
        sets = list(api_set.all())
        for set in sets:
            body = {
                'full_name': set.name,
                'abbreviation': set.code,
                'release_date': set.release_date,
                'type': set.type
            }
            Set.objects.update_or_create(defaults=body, abbreviation=set.code)

    def sync_cards(self):
        sets = Set.objects.all()
        set_matrix = list(self.chunks(sets, 50))
        group_count = 0
        for sets in set_matrix:
            # threads = []
            group_count += 1
            for set in sets:
                self.sync_cards_of_set(set.abbreviation)
                # threads.append(threading.Thread(target=self.sync_cards_of_set, args=(set.abbreviation,)))
            # map(self.execute_thread, threads)
            print('Group {0}/{1}: finished'.format(group_count, len(set_matrix)))
        print('Finished Syncing Cards')

    @staticmethod
    def chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    @staticmethod
    def execute_thread(thread):
        thread.start()
        thread.join()

    @staticmethod
    def sync_cards_of_set(set_code):
        start_time = time.time()
        cards = api_cards.where(set=set_code).all()
        for card in cards:
            set = Set.objects.get(abbreviation=card.set)
            body = {
                'name': card.name,
                'mana_cost': card.mana_cost,
                'converted_mana_cost': card.cmc,
                'abilities': card.text,
                'power': card.power,
                'toughness': card.toughness,
                'loyalty': None if card.loyalty == 0 else card.loyalty,
                'rarity': card.rarity,
                'number': card.number,
                'img_url': card.image_url,
                'type': card.type,
                'flavor_text': card.flavor,
                'set': set
            }
            Card.objects.update_or_create(defaults=body, set_id=set.id, number=card.number)
        end_time = time.time()
        print('{0} seconds to sync set {1} .'.format(end_time - start_time, set_code))

    @staticmethod
    def sync_all_cards():
        start_time = time.time()
        count = 0
        cards = api_cards.all()
        for card in cards:
            set = Set.objects.get(abbreviation=card.set)
            body = {
                'name': card.name,
                'mana_cost': card.mana_cost,
                'converted_mana_cost': card.cmc,
                'abilities': card.text,
                'power': card.power,
                'toughness': card.toughness,
                'loyalty': None if card.loyalty == 0 else card.loyalty,
                'rarity': card.rarity,
                'number': card.number,
                'img_url': card.image_url,
                'type': card.type,
                'flavor_text': card.flavor,
                'set': set
            }
            Card.objects.update_or_create(defaults=body, set_id=set.id, number=card.number)
            count += 1
        end_time = time.time()
        print('{0} seconds to sync {1} cards.'.format(end_time - start_time, count))
