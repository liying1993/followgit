from django.contrib import admin

# Register your models here.
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from account.models import *


# admin.site.register(Profile, ProfileAdmin)