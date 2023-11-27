from rest_framework import serializers
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('team_name', 'team_city')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('player_name', 'team')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('pub_date', 'title', 'content', 'team', 'player')
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_name', 'tag_description', 'articles')
    
class Game(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('game_date', 'home_team', 'opp_team')
    
class Stat(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ('stat_title', 'stat_description', 'stat_value', 'stat_player', 'stat_team')

