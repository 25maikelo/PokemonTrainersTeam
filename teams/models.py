from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import SoftDeletableModel
from core.models import TimeStampedModel


class Trainer(SoftDeletableModel, TimeStampedModel):

    name = models.CharField(max_length=75)

    class Meta:
        verbose_name = _("Trainer")
        verbose_name_plural = _("Trainers")

    def __str__(self):
        return f'{self.name}'


class Pokemon(SoftDeletableModel, TimeStampedModel):

    name = models.CharField(max_length=75)

    class Meta:
        verbose_name = _("Pokemon")
        verbose_name_plural = _("Pokemons")

    def __str__(self):
        return f'{self.name}'


class Team(SoftDeletableModel, TimeStampedModel):

    trainer = models.ForeignKey(
        Trainer,
        related_name='related_trainer',
        on_delete=models.CASCADE
    )
    pokemons = models.ManyToManyField(Pokemon, blank=True)
    name = models.CharField(max_length=75)

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return f'{self.name}'
