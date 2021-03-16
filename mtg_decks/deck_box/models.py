from django.db import models
from django.contrib.auth import get_user_model


class Deck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    user = models.ForeignKey(
        get_user_model(),
        related_name='deck',
        on_delete=models.CASCADE)
    format = models.ForeignKey('Format', null=True, blank=True, related_name='decks',
                               on_delete=models.deletion.PROTECT)
    wins = models.IntegerField(null=False, blank=False, default=0)
    losses = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        db_table = 'deck'


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mana_cost = models.CharField(max_length=255, null=True, blank=True)
    converted_mana_cost = models.IntegerField(null=True, blank=True)
    abilities = models.TextField(null=True, blank=True)
    power = models.CharField(max_length=255, null=True, blank=True)
    toughness = models.CharField(max_length=255, null=True, blank=True)
    loyalty = models.CharField(max_length=255, null=True, blank=True)
    rarity = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=False, blank=False, default=0)
    img_url = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    flavor_text = models.TextField(null=True, blank=True)
    set = models.ForeignKey('Set', null=False, blank=False, related_name='cards', on_delete=models.deletion.PROTECT)

    class Meta:
        db_table = 'card'


class DeckCard(models.Model):
    deck = models.ForeignKey('Deck', null=False, blank=False, related_name='deck_cards', on_delete=models.deletion.PROTECT)
    card = models.ForeignKey('Card', null=False, blank=False, related_name='deck_cards', on_delete=models.deletion.PROTECT)
    amount = models.IntegerField(default=0)
    commander = models.BooleanField(default=False)
    sideboard = models.BooleanField(default=False)

    class Meta:
        db_table = 'deck_card'


class Format(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'format'


class Set(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=10)
    release_date = models.DateField(null=True)
    type = models.CharField(null=True, max_length=64)

    class Meta:
        db_table = 'set'
