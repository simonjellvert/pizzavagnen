from django import forms
from .models import Post
from django.forms import ClearableFileInput


class EventForm(forms.ModelForm):
    """
    Form for creating event
    """

    class Meta:
        model = Post
        fields = [
            'title',
            'event_date',
            'event_description',
            'event_location',
        ]
        

class EditEventForm(forms.ModelForm):
    """
    Form for editing event
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'event_date',
            'event_description',
            'event_location',
        ]
