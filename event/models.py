from django.db import models


class Match(models.Model):

    date = models.DateField()
    first_team = models.ForeignKey('team.Club', on_delete=models.CASCADE, related_name='Matchs_first_team')
    second_team = models.ForeignKey('team.Club', on_delete=models.CASCADE, related_name='Matchs_second_team')
    # total_goals = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.first_team, self.second_team)

    def get_first_team_goals(self):
        goal_event = self.match_details.filter(type='goal', player__club=self.first_team).count()
        return goal_event

    def get_second_team_goals(self):
        goal_event = self.match_details.filter(type='goal', player__club=self.second_team).count()
        return goal_event

    def get_winner_team(self):

        if self.get_first_team_goals() > self.get_second_team_goals():
            return self.first_team

        if self.get_second_team_goals() > self.get_first_team_goals():
            return self.second_team

        if self.get_first_team_goals() == self.get_second_team_goals():
            return None


class MatchDetail(models.Model):

    EVENT_TYPE = (
        ('goal', 'GOAL'),
        ('own_goal', 'OWN GOAL'),
        ('assist', 'ASSIT'),
        ('red_card', 'RED CARD'),
        ('yellow_card', 'YELLOW CARD'),
        ('penalty_success', 'PENALTY SUCCESS'),
        ('penalty_failed', 'PENALTY FAILED'),
    )

    match = models.ForeignKey('event.Match', on_delete=models.CASCADE, related_name='match_details')
    type = models.CharField(max_length=50, choices=EVENT_TYPE)
    player = models.ForeignKey('team.Player', on_delete=models.CASCADE)
    time = models.CharField(max_length=10)
