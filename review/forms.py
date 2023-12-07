from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Review form
    """
    rating = forms.ChoiceField(choices=[
        ('5', '🍕🍕🍕🍕🍕'),
        ('4', '🍕🍕🍕🍕'),
        ('3', '🍕🍕🍕'),
        ('2', '🍕🍕'),
        ('1', '🍕'),
    ], widget=forms.RadioSelect(attrs={'class': 'btn-check'}))

    class Meta:
        model = Review
        fields = ['rating', 'content']


class EditReviewForm(forms.ModelForm):
    """
    Form for editing review
    """
    class Meta:
        model = Review
        fields = ['rating', 'content']
