import requests
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from config.settings.base import API_URL
from .models import Trainer, Pokemon, Team
from .serializers import PokemonSerializer, TrainerSerializer, TeamSerializer

# Trainer Views
class TrainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trainers to be viewed or edited.
    """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

# Team Views
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

# Pokemon Views
class PokemonList(APIView):

    def get(self, request, *args, **kwargs):

        response = requests.get(API_URL)
        pokemons = response.json().get('results')
        for pokemon in pokemons:
            if not Pokemon.objects.filter(name=pokemon.get('name')).exists():
                Pokemon.objects.create(name=pokemon.get('name'))

        queryset = Pokemon.objects.all()
        serializer = PokemonSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
