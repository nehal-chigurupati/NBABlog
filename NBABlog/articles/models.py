from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.TextField()
    team_city = models.TextField()
    team_id = models.IntegerField()

    def __str__(self):
        return self.team_name
    
class Player(models.Model):
    player_name = models.TextField()
    player_id = models.IntegerField()
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
    tag_id = models.IntegerField()
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name

class Stat(models.Model):
    stat_title = models.TextField()
    stat_description = models.TextField()
    stat_id = models.IntegerField()
    stat_value = models.TextField()
    stat_player = models.ForeignKey(Player, on_delete=models.CASCADE)
    stat_team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.stat_title
