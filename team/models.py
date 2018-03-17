from django.db import models
from event.models import Match


class Club(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="uploads/")

    def count_win_amount(self):
        amount = len([match for match in Match.objects.all() if match.get_winner_team() is self])
        return amount

    def count_draw_amount(self):
        amount = len([match for match in Match.objects.all() if match.get_winner_team() is None])
        return amount

    def count_loose_amount(self):
        amount = len([match for match in Match.objects.all() if match.get_winner_team() is not self and match.get_winner_team() is not None])
        return amount

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
        ('d', 'C'),
    )

    club = models.ForeignKey(Club, related_name='players', on_delete=models.CASCADE)

    image = models.ImageField(upload_to="uploads/")
    name = models.CharField(max_length=100)
    player_number = models.IntegerField()
    preferred_foot = models.CharField(max_length=1, choices=PREFERRED_FOOT_TYPE)
    natiolity = models.CharField(max_length=3, choices=NATIOLITY_TYPE)
    injury = models.CharField(max_length=1, choices=INJURY_TYPE)
    balance = models.IntegerField()
    stamina = models.IntegerField()
    passing = models.IntegerField()
    skill = models.IntegerField()
    attack = models.IntegerField()
    dribling = models.IntegerField()
    ability = models.IntegerField()
    defend = models.IntegerField()
