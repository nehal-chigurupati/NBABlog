from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.TextField()
    team_city = models.TextField()

    def __str__(self):
        return self.team_name
    
class Player(models.Model):
    player_name = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_name

class Article(models.Model):
    pub_date = models.DateTimeField("date published")
    title = models.TextField()
    content = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(Player, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.TextField()
    tag_description = models.TextField()
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name

class Game(models.Model):
    game_date = models.DateField("Day of game")
    home_team = models.ForeignKey(Team, on_delete = models.CASCADE, related_name="home_team")
    opp_team = models.ForeignKey(Team, on_delete = models.CASCADE, related_name="opp_team")

    def __str__(self):
        return self.opp_team + " @ " + self.home_team


class Stat(models.Model):
    stat_title = models.TextField()
    stat_description = models.TextField()
    stat_value = models.TextField()
    stat_player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    stat_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    stat_game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.stat_title


