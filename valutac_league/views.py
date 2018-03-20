from django.views.generic import TemplateView
from team.models import Club, Player
from operator import itemgetter


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Club.objects.all()
        context['players'] = Player.objects.all()


        player_goals = [{'player':player, 'goals':player.get_goals()} for player in Player.objects.all()]
        context['player_goals']= sorted(player_goals, key=itemgetter('goals'), reverse=True)

        return context