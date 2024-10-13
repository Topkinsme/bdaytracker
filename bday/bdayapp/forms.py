from django import forms
from django.forms import ModelForm
from .models import Event
from django.contrib.auth.models import User


class EventForm(ModelForm):
    class Meta:
        model=Event
        fields=["person_name","event_type","event_date","author"]
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'})
        }
        
