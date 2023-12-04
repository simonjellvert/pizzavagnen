from django import forms
from .models import Post


class EventForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['featured_image', 'event_date',
                  'event_description', 'event_location']


class EditEventForm(forms.ModelForm):
    """
    Form for editing review
    """
    class Meta:
        model = Post
        fields = ['featured_image', 'event_date',
                  'event_description', 'event_location']
