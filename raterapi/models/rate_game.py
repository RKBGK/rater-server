
from django.db import models

from raterapi.models.game import Game
from raterapi.models.player import Player

class RateGame(models.Model):
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField()