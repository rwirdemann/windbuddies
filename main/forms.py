from django.forms import ModelForm
from .models import Session, Spot
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SessionForm(ModelForm):
    spot = forms.ModelChoiceField(queryset=Spot.objects.all(),
                                  empty_label="Wähle deinen Spot...",
                                  required=True)
    when = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': "Wann geht's los?"
        }))

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