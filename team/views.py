import datetime
from django.views.generic import DetailView
from django.db.models import Q
from .models import Club, Player
from team.models import Match
from django.db.models.functions import TruncMonth, TruncDate

class ClubView(DetailView):
    model = Club
    template_name = 'club.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['matches'] = []

        club = self.get_object()
        dates = []
        for match in club.get_matches():
            match_date = match.date.strftime("%d/%m/%Y")

            if match_date not in dates:
                dates.append(match_date)

        for date in dates:
            date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
            context['matches'].append({"date":date, 'matches':club.get_matches().filter(date=date)})

        return context


class PlayerView(DetailView):
    model = Player
    template_name = 'player.html'