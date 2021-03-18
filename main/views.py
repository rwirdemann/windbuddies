from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import requests
import datetime

from .models import Session
from .forms import SessionForm


def index(request):
    sessions = Session.objects.order_by('when')[:8]
    context = {'latest_sessions': sessions}
    return render(request, 'main/index.html', context)


def create(request):
    if request.method == 'POST':
        f = SessionForm(request.POST)
        f.save()
        return HttpResponseRedirect('/main')
    else:
        form = SessionForm()

    return render(request, 'main/session.html', {'form': form})

def delete_session(request, session_id):
    s = Session.objects.get(id=session_id)
    if s is not None:        
        s.delete()

    return HttpResponseRedirect('/main')


def actual_weather(request):
    json = requests.get(
        'https://9nehnu4h6h.execute-api.us-east-1.amazonaws.com/stage/').text
    return HttpResponse(json, content_type='application/json')