import requests
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from config.settings.base import API_URL
from .models import Trainer, Pokemon, Team
from .serializers import TrainerSerializer, PokemonSerializer, TeamSerializer

def pokemons_decorator(call):

    def get_pokemons():

        response = requests.get(API_URL)
        pokemons = response.json()
        for pokemon in pokemons:
            if not Pokemon.objects.filter(name=pokemon.get('name')):
                Pokemon.objects.create(name=pokemon.get('name'))

    return get_pokemons


class TrainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trainers to be viewed or edited.
    """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    response = requests.get(API_URL)
    pokemons = response.json().get('results')
    for pokemon in pokemons:
        if not Pokemon.objects.filter(name=pokemon.get('name')).exists():
            Pokemon.objects.create(name=pokemon.get('name'))
