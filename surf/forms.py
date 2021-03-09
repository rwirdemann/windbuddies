from django import forms

class SessionForm(forms.Form):
    spot = forms.CharField(label='Wo', max_length=100)
    when = forms.DateField(label='Wann')