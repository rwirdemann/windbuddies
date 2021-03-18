from django.forms import ModelForm
from .models import Session
from django import forms
import django.utils.timezone


class SessionForm(ModelForm):
    spot = forms.CharField(
        max_length=50,
        label='Wo',
        widget=forms.TextInput(attrs={
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
