from django import forms
from .models import Post
from django.forms import ClearableFileInput


class EventForm(forms.ModelForm):

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
    Form for editing review
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'event_date',
            'event_description',
            'event_location',
        ]
