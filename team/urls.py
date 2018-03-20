from django.urls import path
from .views import ClubView, PlayerView

urlpatterns = [
    path('club/<pk>/', ClubView.as_view(), name='club-detail'),
    path('player/<pk>/', PlayerView.as_view(), name='player-detail')
]