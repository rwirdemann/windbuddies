from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
import requests
from .models import Session
from .forms import SessionForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(
                request,
                "Du hast dich erfolgreich registriert und bist jetzt eingelogged!"
            )
            return redirect('index')
    else:
        m = ("Windbuddies setzt auf Datensparsamkeit. Wir wollen so wenig wie möglich von Dir wissen "
             "und beschränken uns deshalb auf Name und Passwort. Wählst Du einen Fantasienamen, dann nutzt "
             "Du Windbuddies quasi annonym. Nur Deine Freunde wissen wer du bist, weil Du ihnen "
             "Deinen Windbuddies-Namen am Strand verraten hast.")
        messages.success(
            request,
            m
        )
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})