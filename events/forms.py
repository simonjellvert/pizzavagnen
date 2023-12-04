from django import forms
from .models import Post
from cloudinary.forms import CloudinaryJsFileField
from django.forms import ClearableFileInput


class EventForm(forms.ModelForm):

    featured_image = CloudinaryJsFileField(widget=ClearableFileInput)

    class Meta:
        model = Post
        fields = [
            'title',
            'event_date',
            'event_description',
            'event_location',
            'featured_image'
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
            'featured_image'
        ]
