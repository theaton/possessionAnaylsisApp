from django.shortcuts import *
from .models import *


def game_log(request):
    games = Game.objects.all()
    return render(request, 'logger/game_log.html', {'games': games})


def index(request, game_id):
    games = Game.objects.all()
    players = Player.objects.all()
    teams = Team.objects.all()
    game_id = get_object_or_404(Game, id=games)
    return render(request, 'logger/index.html', {'games': games, 'players': players, 'teams': teams, 'game_id': game_id})
