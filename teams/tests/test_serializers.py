from django.test import TestCase
from teams.serializers import TrainerSerializer, PokemonSerializer, TeamSerializer
from teams.tests.factories import TrainerFactory, PokemonFactory, TeamFactory


class TrainerSerializerTestCase(TestCase):

    def test_model_fields(self):
        trainer = TrainerFactory()
        serializer = TrainerSerializer(trainer, read_only=True)
        self.assertEqual(serializer.data.get('name'), getattr(trainer, 'name'))


class PokemonSerializerTestCase(TestCase):

    def test_model_fields(self):
        pokemon = PokemonFactory()
        serializer = PokemonSerializer(pokemon, read_only=True)
        self.assertEqual(serializer.data.get('name'), getattr(pokemon, 'name'))


class TeamSerializerTestCase(TestCase):

    def test_model_fields(self):
        team = TeamFactory()
        serializer = TeamSerializer(team, read_only=True)
        self.assertEqual(serializer.data.get('name'), getattr(team, 'name'))
