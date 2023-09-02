# Django Imports
from django.contrib import admin


# Inside Project Imports
from .models import Band, Artist, Listener


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ("name", "started_at", "end_at")


admin.site.register(Artist)
admin.site.register(Listener)
