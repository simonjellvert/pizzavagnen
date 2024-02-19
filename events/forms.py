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
            'featured_image',
        ]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

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
            'featured_image',
        ]

    def __init__(self, *args, **kwargs):
        super(EditEventForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True