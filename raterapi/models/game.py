from django.db import models

from raterapi.models.game_type import GameType
from raterapi.models.player import Player

# installed pillow library

class Game(models.Model):
    
    title= models.CharField(max_length=50)
    maker= models.CharField(max_length=50)
    release_date= models.DateField()
    game_image= models.ImageField(upload_to ='uploads/', default=None) 
    game_url = models.URLField(max_length=500, default=None)
    game_type= models.ForeignKey(GameType, on_delete=models.CASCADE)
    registrant= models.ForeignKey(Player, on_delete=models.CASCADE)
    
    
    