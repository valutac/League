import locale
from django.db import models
from django.db.models import Q
from event.models import Match, MatchDetail


class Club(models.Model):
    NATIOLITY_TYPE = (
        ('id', 'INDONESIA'),
    )

    name = models.CharField(max_length=50)
    founded_year = models.IntegerField()
    natiolity = models.CharField(max_length=5, choices=NATIOLITY_TYPE)
    description = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.name

    def get_win_amount(self):
        amount = 0
        for match in Match.objects.filter(Q(first_team_id=self.id)|Q(second_team_id=self.id)):
            if match.get_winner_team() is not None and match.get_winner_team().id == self.id:
                amount+=1
        return amount

    def get_draw_amount(self):
        amount = 0
        for match in Match.objects.filter(Q(first_team_id=self.id)|Q(second_team_id=self.id)):
            if match.get_winner_team() is None:
                amount += 1
        return amount

    def get_loose_amount(self):
        amount = 0
        for match in Match.objects.filter(Q(first_team_id=self.id)|Q(second_team_id=self.id)):
            if match.get_winner_team() is not None and match.get_winner_team().id != self.id:
                amount+=1
        return amount

    def get_goal_for(self):
        goals_for = [match for match in MatchDetail.objects.filter(player__club_id=self.id)]
        return len(goals_for)

    def get_goal_against(self):
        amount = 0

        for match in self.Matchs_first_team.all():
            amount += match.get_second_team_goals()

        for match in self.Matchs_second_team.all():
            amount += match.get_first_team_goals()

        return amount

    def get_goal_differents(self):
        return self.get_goal_for() - self.get_goal_against()

    def get_points(self):
        points = 0
        points += self.get_win_amount() * 3
        points += self.get_draw_amount() * 1
        return points

    def get_matches(self):
        matches = Match.objects.filter(Q(first_team_id=self.id) | Q(second_team_id=self.id))
        return matches


class Player(models.Model):
    PREFERRED_FOOT_TYPE = (
        ('l', 'LEFT'),
        ('r', 'RIGHT'),
        ('b', 'BOTH')
    )

    NATIOLITY_TYPE = (
        ('id', 'INDONESIA'),
    )

    INJURY_TYPE = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )

    POSITION_CODE_TYPE = (
        ('cf', 'CF'),
        ('mf', 'MF'),
        ('cb', 'CB')
    )

    club = models.ForeignKey(Club, related_name='players', on_delete=models.CASCADE)

    image = models.ImageField(upload_to="uploads/")
    name = models.CharField(max_length=100)
    player_number = models.IntegerField()
    preferred_foot = models.CharField(max_length=1, choices=PREFERRED_FOOT_TYPE)
    natiolity = models.CharField(max_length=3, choices=NATIOLITY_TYPE)
    injury = models.CharField(max_length=1, choices=INJURY_TYPE)
    position_name = models.CharField(max_length=50)
    position_code = models.CharField(max_length=5, choices=POSITION_CODE_TYPE)

    balance = models.IntegerField()
    stamina = models.IntegerField()
    passing = models.IntegerField()
    shooting = models.IntegerField()
    skill = models.IntegerField()
    attack = models.IntegerField()
    dribbling = models.IntegerField()
    ability = models.IntegerField()
    defend = models.IntegerField()

    def __str__(self):
        return self.name

    def get_goals(self):
        amount = MatchDetail.objects.filter(player_id=self.id, type='goal').count()
        return amount

    def get_own_goals(self):
        amount = MatchDetail.objects.filter(player_id=self.id, type='own_goal').count()
        return amount

    def get_assists(self):
        amount = MatchDetail.objects.filter(player_id=self.id, type='assist').count()
        return amount

    def get_red_cards(self):
        amount = MatchDetail.objects.filter(player_id=self.id, type='red_card').count()
        return amount

    def get_yellow_cards(self):
        amount = MatchDetail.objects.filter(player_id=self.id, type='yellow_card').count()
        return amount

    def get_penalty_success(self):
        amount = MatchDetail.objects.filter(player_id=self.id, type='penalty_success').count()
        return amount

    def get_penalty_failed(self):
        amount = MatchDetail.objects.filter(player_id=self.id, type='penalty_failed').count()
        return amount

    def get_overall_amount(self):
        amount = [self.balance, self.stamina, self.passing, self.shooting, self.skill, self.attack, self.dribbling, self.ability, self.defend]
        return locale.format('%.2f', sum(amount)/len(amount))