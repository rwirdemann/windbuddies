from django import forms

class SessionForm(forms.Form):
    spot = forms.CharField(label='Der Spot', max_length=100)
