from dataclasses import field
import imp
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from raterapi.models.player import Player

class PlayerView(ViewSet):
    """Players"""
    def list(self, request):
        player = Player.objects.all()
        serializer = PlayerSeriallizer(player, many=True)
        return Response(serializer.data)
        
class PlayerSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id','bio')
        depth = 2
        