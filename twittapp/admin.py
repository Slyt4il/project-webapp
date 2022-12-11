from csv import list_dialects
from django.contrib import admin

from .models import *

class TwittAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__user__username']
    class META:
        model = Twitt

admin.site.register(Twitt, TwittAdmin)