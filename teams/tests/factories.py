from mimetypes import suffix_map
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from teams.models import Trainer, Pokemon, Team

class TrainerFactory(DjangoModelFactory):

    name = Faker('first_name')

    class Meta:
        model = Trainer


class PokemonFactory(DjangoModelFactory):

    name = Faker('first_name')

    class Meta:
        model = Pokemon


class TeamFactory(DjangoModelFactory):

    trainer = SubFactory(TrainerFactory)
    name = Faker('first_name')

    class Meta:
        model = Team
