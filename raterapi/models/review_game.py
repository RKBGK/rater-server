from django.db import models

from raterapi.models.game import Game
from raterapi.models.player import Player

class ReviewGame(models.Model):
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=100)