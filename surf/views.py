from django.shortcuts import render
from django.views import generic

from .models import Session

class IndexView(generic.ListView):
    template_name = 'surf/index.html'
    context_object_name = 'latest_sessions'

    def get_queryset(self):
        return Session.objects.order_by('-when')[:5]
