from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .models import Session
from .forms import SessionForm

class IndexView(generic.ListView):
    template_name = 'surf/index.html'
    context_object_name = 'latest_sessions'

    def get_queryset(self):
        return Session.objects.order_by('-when')[:5]

def create_session(request):
    form = SessionForm(request.POST)
    s = Session(spot=form.data['spot'], when=form.data['when'])
    s.save() 
    return HttpResponseRedirect('/surf')