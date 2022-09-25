from django.db import models
from django.utils.translation import gettext as _

"""
    An abstract base class model that provides self-updating ``created`` and ``modified`` fields.
"""
class TimeStampedModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
