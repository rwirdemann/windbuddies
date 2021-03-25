from django.forms import ModelForm
from .models import Session
from django import forms
import django.utils.timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SessionForm(ModelForm):
    spot = forms.CharField(max_length=50,
                           label='Wo',
                           widget=forms.TextInput(
                               attrs={
                                   'autofocus': True,
                                   'placeholder': 'Name des Spots',
                                   'class': 'form-control'
                               }))
    when = forms.CharField(widget=forms.SelectDateWidget(),
                           label='Wann',
                           initial=django.utils.timezone.now())

    class Meta:
        model = Session
        fields = ['spot', 'when']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]
