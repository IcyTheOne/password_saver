from django.contrib import admin

# Register your models here.

from .models import SavedAccount

admin.site.register(SavedAccount)
