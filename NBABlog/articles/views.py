from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is where all my articles will be listed.")

def article(request, article_id):
    return HttpResponse("You've accessed article " + str(article_id))

def tag(request, tag_id):
    return HttpResponse("You've accessed articles for tag " + str(tag_id))

def team_page(request, team_id):
    return HttpResponse("You've accessed the team page for team " + str(team_id))

def player_page(request, player_id):
    return HttpResponse("You've accessed the player page for " + str(player_id))

