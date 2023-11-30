from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for creating a review
    """
    class Meta:
        model = Review
        fields = ['content', 'rating']


class EditReviewForm(forms.ModelForm):
    """
    Form for editing review
    """
    class Meta:
        model = Review
        fields = ['content', 'rating']
