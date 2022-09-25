# -*- coding: utf-8 -*-

from .base import *

"""
***********************
*   Force SSL/HTTPS   *
***********************
"""

"""
********************************
* PRODUCTION MIDDLEWARE ADDITION *
********************************
"""

MIDDLEWARE += [
]

"""
*************************
* DEVELOP APPS ADDITION *
*************************
"""

INSTALLED_APPS += [
    'django_extensions',
]

"""
###############################
# TEMPLATES ADDITION SETTINGS #
###############################
"""

TEMPLATES[0]['OPTIONS']['context_processors'] += [

]
