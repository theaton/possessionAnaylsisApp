from django.db import models


class Team(models.Model):
    team_city = models.CharField(max_length=30)
    team_nickname = models.CharField(max_length=30)


class Game(models.Model):
    date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()


class Position(models.Model):
    Positions = (
        ('1', 'Point Guard'),
        ('2', 'Shooting Guard'),
        ('3', 'Small Forward'),
        ('4', 'Power Forward'),
        ('5', 'Center'),
    )
    player_position = models.CharField(max_length=1, choices=Positions)


class Player(models.Model):
    player_name = models.CharField(max_length=80)
    player_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Pass(models.Model):
    pass_type = models.CharField(max_length=30)
    pass_detail_type = models.CharField(max_length=30)
    pass_quality = models.CharField(max_length=30)


class Screen(models.Model):
    screen_type = models.CharField(max_length=30)
    screen_detail_type = models.CharField(max_length=30)
    screen_quality = models.CharField(max_length=30)


class Shot(models.Model):
    shot_type = models.CharField(max_length=30)
    shot_detail_type = models.CharField(max_length=30)
    shot_quality = models.CharField(max_length=30)


class Cut(models.Model):
    cut_type = models.CharField(max_length=30)
    cut_detail_type = models.CharField(max_length=30)
    cut_quality = models.CharField(max_length=30)


class Possession(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    teams = models.ForeignKey(Team, on_delete=models.CASCADE)
    players = models.ForeignKey(Player, on_delete=models.CASCADE)
    passes = models.ForeignKey(Pass, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    shot = models.ForeignKey(Shot, on_delete=models.CASCADE)
    cut = models.ForeignKey(Cut, on_delete=models.CASCADE)
