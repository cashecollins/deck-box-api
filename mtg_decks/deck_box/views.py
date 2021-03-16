from django.shortcuts import render


# Create your views here.
from deck_box.models import Deck


def deck_details(request, pk):
    deck_obj = Deck.objects.get(pk=pk)
    context = {
        "deck": deck_obj,
        "cards": deck_obj.deck_cards.all()
    }

    return render(request, '../templates/deck_details.html', context)
