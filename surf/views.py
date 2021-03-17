from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import requests

from .models import Session
from .forms import SessionForm


def index(request):
    sessions = Session.objects.order_by('-when')[:5]

    context = {'latest_sessions': sessions}
    return render(request, 'surf/index.html', context)


def create_session(request):
    form = SessionForm(request.POST)
    s = Session(spot=form.data['spot'], when=form.data['when'])
    s.save()
    return HttpResponseRedirect('/surf')


def actual_weather(request):
    json = requests.get('https://9nehnu4h6h.execute-api.us-east-1.amazonaws.com/stage/').text
    return HttpResponse(json, content_type='application/json')