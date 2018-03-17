from django.contrib import admin
from .models import Match, MatchDetail


class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'first_team', 'second_team', 'total_goals')


class MatchDetailAdmin(admin.ModelAdmin):
    list_display = ('type', 'team', 'player', 'time')


admin.site.register(Match, MatchAdmin)
admin.site.register(MatchDetail, MatchDetailAdmin)