from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is where all my articles will be listed.")

def article(request, article_id):
    return HttpResponse("You've accessed article " + str(article_id))
