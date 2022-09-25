from rest_framework import serializers
from .models import Trainer, Pokemon, Team


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = '__all__'

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

    def validate(self, data):
        if len(data['pokemons']) > 6:
            raise serializers.ValidationError({"pokemons": "Max 6 pokemons allowed"})
        return data
