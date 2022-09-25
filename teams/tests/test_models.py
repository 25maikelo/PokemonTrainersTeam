from django.test import TestCase
from teams.tests.factories import TrainerFactory, PokemonFactory, TeamFactory


class TrainerTestCase(TestCase):

    def test_str(self):
        trainer = TrainerFactory()
        self.assertEqual(str(trainer), trainer.name)


class PokemonTestCase(TestCase):

    def test_str(self):
        pokemon = PokemonFactory()
        self.assertEqual(str(pokemon), pokemon.name)


class TeamTestCase(TestCase):

    def test_str(self):
        team = TeamFactory()
        self.assertEqual(str(team), team.name)
