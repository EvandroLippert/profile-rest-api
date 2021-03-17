"""

Para acessar os models criados na página admin do django
é necessário adicioná-los aqui

"""
from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
