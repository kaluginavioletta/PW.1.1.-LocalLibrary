from django.http import HttpResponse

from django.shortcuts import render
from .models import Team

def index(request):
    return HttpResponse('Hello from Django!')

def index(request):
    list_teams = Team.objects.filter(team_level__exact="U09")
    context = {'youngest_teams': list_teams}
    return render(request, '/best/index.html', context)