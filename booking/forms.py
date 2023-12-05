from datetime import date
from django import forms
from django.forms import DateInput, TimeInput
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Booking form for the user
    """
    class Meta:
        model = Booking
        min_date = date.today()
        fields = ['date', 'time', 'location']
        widgets = {
            'date': DateInput(attrs={
                'class': 'datepicker',
                'type': 'date',
                'min': str(min_date)}),
            'ime': TimeInput(attrs={
                'class': 'timepicker',
                'min': '12:00',
                'max': '23:00',
                'type': 'time',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['min'] = str(date.today())
