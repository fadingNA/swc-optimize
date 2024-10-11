from django.urls import path
from .views import get_routes, get_monsters, get_monster_detail, HomePageView, rune_interface

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('runes/', rune_interface, name='rune_interface'),
    path('chat_with_optimizer', get_runes_by_set, name='get_runes_by_set'),
    path('monsters/', get_monsters, name='get_monsters'),
    path('monsters/<int:monster_id>/', get_monster_detail, name='get_monster_detail'),
]