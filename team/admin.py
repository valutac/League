from django.contrib import admin
from .models import Club, Player


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('club', 'image', 'name', 'player_number')

admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)