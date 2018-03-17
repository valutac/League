from django.db import models
from team.models import Player, Club


class Match(models.Model):

    date = models.DateField()
    first_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='Matchs_first_team')
    second_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='Matchs_second_team')
    total_goals = models.IntegerField()

    def get_winner_team(self):
        first_team_goals = MatchDetail.objects.filter(type='goal', team=1)
        second_team_goals = MatchDetail.objects.filter(type='goal', team=2)

        if first_team_goals > second_team_goals:
            return self.first_team
        else:
            return self.sec

        return None


class MatchDetail(models.Model):

    EVENT_TYPE = (
        ('goal', 'GOAL'),
        ('assist', 'ASSIT'),
        ('red_card', 'RED CARD'),
        ('yellow_card', 'YELLOW CARD'),
        ('penalty_success', 'PENALTY SUCCESS'),
        ('penalty_failed', 'PENALTY FAILED'),
    )

    TEAMS = (
        (1, 'Team 1'),
        (2, 'Team 2')
    )
    type = models.CharField(max_length=50, choices=EVENT_TYPE)
    team = models.IntegerField(choices=TEAMS)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    time = models.CharField(max_length=10)
