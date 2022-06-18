from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from raterapi.models import GameType, Player, Game

class GameView(ViewSet)       :
    """game types"""
    def retrieve(self, request, pk):
        games= Game.objects.get(pk=pk)
        serializer = GameSerializer(games)
        return Response(serializer.data)
    
    def list(self, request):
        games = Game.objects.all()
        game_type = request.query_params.get('type', None)
        if game_type is not None:
            games = games.filter(game_type_id=game_type)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    def create(self, request):
        registrant = Player.objects.get(user=request.auth.user)
        serializer = CreatteGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(registrant=registrant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ('id', 'title','maker','release_date','game_image','game_url', 'game_type','registrant','categories')
        depth = 2
        
class CreatteGameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ('id', 'title','maker','release_date','game_image','game_url', 'game_type')
        