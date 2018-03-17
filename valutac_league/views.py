from django.views.generic import TemplateView
from team.models import Club, Player


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Club.objects.all()
        return context