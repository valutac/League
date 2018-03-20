from django.contrib import admin
from .models import Match, MatchDetail


class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'first_team', 'second_team')


class MatchDetailAdmin(admin.ModelAdmin):
    list_display = ('type', 'player', 'time')


admin.site.register(Match, MatchAdmin)
admin.site.register(MatchDetail, MatchDetailAdmin)